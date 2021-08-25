from argparse import ArgumentParser
from bs4 import BeautifulSoup  # type: ignore
from dateutil import parser as dparser
from requests import get as rqget  # type: ignore
from helpers.connection import db  # type: ignore
import locale

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

parser = ArgumentParser()
parser.add_argument("--force", action="store_true")
args = parser.parse_args()

tables = db.scrape_tables.find_one()
covid_data = db.covid_data.find_one()
tweets = db.tweet_status.find_one()

for page_name, page in tables["tables"].items():
    soup = BeautifulSoup(
        rqget(
            f"https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/{page['url']}",
            allow_redirects=True,
        ).content,
        features="html.parser",
    )

    # find date callout at top of page and find date using fuzzy search
    date = dparser.parse(soup.find("div", {"class": "well well-sm"}).text, fuzzy=True)
    print(f"Found date for {page_name}: {date.isoformat()}")

    # check data has actually been updated
    if date.isoformat() == tweets["tweets"][page_name]["updated"]:
        if not args.force:
            print("No date update, aborting")
            continue

    # set new date and set posted flags to false
    print(
        f"Updated {page_name} data: {tweets['tweets'][page_name]['updated']} => {date.isoformat()}"
    )
    tweets["tweets"][page_name]["updated"] = date.isoformat()
    for posted in tweets["tweets"][page_name]["tweeted"]:
        tweets["tweets"][page_name]["tweeted"][posted] = False

    for header, tables in page["headers"].items():

        # find section header
        header = soup.find(text=header)
        for table_header in tables:
            # find table header
            table = header.find_next(text=table_header).parent.parent

            # format to json
            covid_data["covid_data"][page_name][header] = {
                header.text: {
                    row.find_all(["th", "td"])[0].text: locale.atoi(
                        row.find_all(["th", "td"])[index].text
                    )
                    for row in table.tbody.find_all("tr")
                }
                for index, header in enumerate(table.thead.find_all("th")[1:], start=1)
            }
    print(f"Scraping {header}")

db.covid_data.update_one({"_id": covid_data["_id"]}, {"$set": covid_data}, upsert=True)
db.tweet_status.update_one({"_id": tweets["_id"]}, {"$set": tweets}, upsert=True)
print("Update complete.")
