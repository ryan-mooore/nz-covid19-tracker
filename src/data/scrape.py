from argparse import ArgumentParser
from json import dumps, loads
from os import environ
from sys import exit as sysexit

import tweepy as tp  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
from dateutil import parser as dparser
from requests import get as rqget  # type: ignore

parser = ArgumentParser()
parser.add_argument("--dev", action="store_true")
args = parser.parse_args()

soup = BeautifulSoup(
    rqget(
        "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-vaccine-data#total-vaccinations",
        allow_redirects=True,
    ).content,
    features="html.parser",
)


status = loads(open("src/data/status.json", "r").read())

header = soup.find(text="COVID-19 vaccinations: daily updates")
date = dparser.parse(header.find_next("div").text, fuzzy=True)

if args.dev:
    print("Skipping data check, dev environment")
elif date.isoformat() == status["last_updated"]:
    print("No data update, aborting")
    sysexit()
else:
    print(f"Updated data: {date}")
    status["last_updated"] = date.isoformat()
    for posted in status["posted"].values():
        posted = False

table = soup.find().find_next("table")

status["data"]["vaccines"] = {
    header.text: {
        row.find_all("td")[0].text: int(row.find_all("td")[index].text)
        for row in table.tbody.find_all("tr")
    }
    for index, header in enumerate(table.find_all("th")[1:], start=1)
}

open("src/data/status.json", "w").write(dumps(status))
