from json import loads, dumps
from os import environ
from datetime import datetime
from sys import argv
from typing import Type
import tweepy as tp  # type: ignore
from importlib import import_module

from helpers.connection import db  # type: ignore

auth = tp.OAuthHandler(environ["CONSUMER_KEY"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["ACCESS_TOKEN"], environ["ACCESS_TOKEN_SECRET"])
api = tp.API(auth)

tweets = db.tweet_status.find_one()
covid_data = db.covid_data.find_one()

for name, tweet_type in tweets["tweets"].items():
    for script, tweeted in tweet_type["tweeted"].items():
        if script == argv[1]:
            if tweeted:
                print(
                    f"Tried to tweet {script} but already tweeted since last data update."
                )
                break
            else:
                tweets["tweets"][name]["tweeted"][script] = True
            print(f"Tweeting {script}...")
            try:
                status = "\n".join(
                    import_module(".".join(["tweets", name, script])).tweet(
                        covid_data["covid_data"]
                    )
                )
            except TypeError:
                print(f"Aborted tweeting {script}...")
                break

            print(f"Tweeted: \n{status}")
            # api.update_status(status)
            break
    else:
        continue
    break
else:
    print(f"Tweet {argv[1]} could not be found in status.json")

db.tweet_status.update_one({"_id": tweets["_id"]}, {"$set": tweets})
