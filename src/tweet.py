from json import loads, dumps
from os import environ
from datetime import datetime
from typing import Type
import tweepy as tp  # type: ignore
from importlib import import_module
from argparse import ArgumentParser
from helpers.connection import db  # type: ignore

auth = tp.OAuthHandler(environ["CONSUMER_KEY"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["ACCESS_TOKEN"], environ["ACCESS_TOKEN_SECRET"])
api = tp.API(auth)

parser = ArgumentParser()
parser.add_argument("tweet")
parser.add_argument("--test", action="store_true")
args = parser.parse_args()

tweets = db.tweet_status.find_one()
covid_data = db.covid_data.find_one()

for name, tweet_type in tweets["tweets"].items():
    for script, tweeted in tweet_type["tweeted"].items():
        if script == args.tweet:
            if args.test:
                print("Running test tweet")
            else:
                if tweeted:
                    print(f"Tweet already posted since {tweet_type['updated']}")
                    print("Exiting")
                    break
                else:
                    print("Tweeting to status")

            try:
                status = "\n".join(
                    import_module(".".join(["tweets", name, script])).tweet(
                        covid_data["covid_data"]
                    )
                )
            except TypeError:
                print(f"Exiting")
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
