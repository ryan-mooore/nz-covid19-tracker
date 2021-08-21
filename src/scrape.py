from argparse import ArgumentParser
from json import dumps, loads

from bs4 import BeautifulSoup  # type: ignore
from dateutil import parser as dparser
from requests import get as rqget  # type: ignore

parser = ArgumentParser()
parser.add_argument("--dev", action="store_true")
args = parser.parse_args()


tables = loads(open("src/data/tables.json", "r").read())
status = loads(open("src/data/status.json", "r").read())

for page_name, page in tables["pages"].items():
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

    if args.dev:
        print("Skipping data check, dev environment")
    # check data has actually been updated
    elif date.isoformat() == status["pages"][page_name]["last_updated"]:
        print("No date update, aborting")
        continue

    # set new date and set posted flags to false
    print(
        f"Updated {page_name} data: {status['pages'][page_name]['last_updated']} => {date.isoformat()}"
    )
    status["pages"][page_name]["last_updated"] = date.isoformat()
    for posted in status["tweeted"][page_name].values():
        posted = False

    for header, tables in page["headers"].items():

        # find section header
        header = soup.find(text=header)
        for table_header in tables:
            # find table header
            table = header.find_next(text=table_header).parent.parent

            # format to json
            status["pages"][page_name][header] = {
                header.text: {
                    row.find_all(["th", "td"])[0].text: int(
                        row.find_all(["th", "td"])[index].text
                    )
                    for row in table.tbody.find_all("tr")
                }
                for index, header in enumerate(table.thead.find_all("th")[1:], start=1)
            }
        print(f"Scraping {header}")

open("src/data/status.json", "w").write(dumps(status))
print("Update complete.")
