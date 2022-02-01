"""Scrapes MoH latest vaccine data tables and updates database."""

import locale
from argparse import ArgumentParser
from typing import Union

from bs4 import BeautifulSoup  # type: ignore
from dateutil import parser as dparser
from requests import get as rqget  # type: ignore

from helpers.connection import db  # type: ignore

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

parser = ArgumentParser()
parser.add_argument("--force", action="store_true")
args = parser.parse_args()

tables = db.scrape_tables.find_one()
covid_data = db.covid_data.find_one()
tweet_data = db.tweet_status.find_one()

table_cells = ["th", "td"]


def _parse_number(number: str) -> Union[float, int, None]:
    if number:
        if "%" in number:
            return locale.atof(number[:-1])
        return locale.atoi(number)
    return None


for page_name, page in tables["tables"].items():
    soup = BeautifulSoup(
        rqget(
            f"https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/{page['url']}",  # noqa
            allow_redirects=True,
        ).content,
        features="html.parser",
    )

    # find date callout at top of page and find date using fuzzy search
    date = dparser.parse(
        soup.find(
            "div", {
                "class": "well well-sm",
            },
        ).text, fuzzy=True,
    )
    print(f"Found date for {page_name}: {date.isoformat()}")

    tweets = tweet_data["tweets"]

    # check data has actually been updated
    if date.isoformat() == tweets[page_name]["updated"]:
        if not args.force:
            print("No date update, aborting")
            continue

    # set new date and set posted flags to false
    print(
        f"Updated {page_name} data: {tweets[page_name]['updated']} "
        f"=> {date.isoformat()}",
    )
    tweet_data["tweets"][page_name]["updated"] = date.isoformat()
    for posted in tweet_data["tweets"][page_name]["tweeted"]:
        tweets[page_name]["tweeted"][posted] = False

    for header, page_tables in page["headers"].items():
        print(f"Scraping {header}")

        # find section header
        header_element = soup.find(text=header)
        for table_header in page_tables:
            # find table header
            table_header_element = header_element.find_next(text=table_header)

            # fix inconsistencies between header types on different pages
            if table_header_element.parent.parent.name == "table":
                table = table_header_element.parent.parent
            else:
                table = table_header_element.parent.find_next("table")

            headings = table.thead.find_all("th")[1:]

            # format to json
            covid_data["covid_data"][page_name][table_header] = {
                header.text: {
                    row.find_all(table_cells)[0].text: _parse_number(
                        row.find_all(table_cells)[index].text,
                    )
                    if len(row.find_all(table_cells)) > index
                    else None
                    for row in table.tbody.find_all("tr")
                }
                for index, header in enumerate(headings, start=1)
            }

db.covid_data.update_one(
    {"_id": covid_data["_id"]},
    {"$set": covid_data},
    upsert=True,
)
db.tweet_status.update_one(
    {"_id": tweet_data["_id"]},
    {"$set": tweet_data},
    upsert=True,
)
print("Update complete.")
