"""Provides an interface to tweet a specific status from stdin."""

from argparse import ArgumentParser
from enum import Enum
from importlib import import_module
from os import environ

import tweepy as tp  # type: ignore

from helpers.connection import db  # type: ignore

auth = tp.OAuthHandler(environ["CONSUMER_KEY"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["ACCESS_TOKEN"], environ["ACCESS_TOKEN_SECRET"])
api = tp.API(auth)

parser = ArgumentParser()
parser.add_argument("tweet")
parser.add_argument("--test", action="store_true")
args = parser.parse_args()


class Population(Enum):
    """Enum storing population estimates as of 30 June 2021."""

    # taken from
    # https://www.stats.govt.nz/information-releases/national-population-estimates-at-30-june-2021
    # (https://www.stats.govt.nz/assets/Uploads/National-population-estimates/National-population-estimates-At-30-June-2021/Download-data/national-population-estimates-at-30-june-2021.xlsx)
    TOTAL = 5122600
    # taken from
    # https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-vaccine-data#details-of-vaccine-data
    # (https://www.health.govt.nz/system/files/documents/pages/covid_vaccinations_26_10_2021.xlsx)
    ELIGIBLE = (4209057 + 476294)  # population + 5-11 population


tweets = db.tweet_status.find_one()
covid_data = db.covid_data.find_one()

for name, tweet_type in tweets["tweets"].items():
    for script, tweeted in tweet_type["tweeted"].items():
        if script == args.tweet:
            if args.test:
                print("Running test tweet")
            else:
                if tweeted:
                    print(
                        f"Tweet already posted since {tweet_type['updated']}")
                    print("Exiting")
                    break
                else:
                    print("Tweeting to status")

            try:
                status = "\n".join(
                    import_module(".".join(["tweets", name, script])).tweet(
                        covid_data["covid_data"],
                        Population,
                    ),
                )
            except TypeError:
                print("Exiting")
                break

            if args.test:
                print(f"Test tweet: \n{status}")
            else:
                # set tweeted to true
                api.update_status(status)
                tweets["tweets"][name]["tweeted"][script] = True
                print(f"Tweeted: \n{status}")
            break
    else:
        continue
    break
else:
    print(f"Tweet {args.tweet} could not be found in status.json")

db.tweet_status.update_one({"_id": tweets["_id"]}, {"$set": tweets})
