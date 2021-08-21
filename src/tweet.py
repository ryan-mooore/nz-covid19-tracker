from json import loads, dumps
from os import environ
from datetime import datetime
from sys import argv
import tweepy as tp  # type: ignore
from importlib import import_module

auth = tp.OAuthHandler(environ["CONSUMER_KEY"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["ACCESS_TOKEN"], environ["ACCESS_TOKEN_SECRET"])
api = tp.API(auth)

data = loads(open("src/data/status.json", "r").read())

for tweet_type, scripts in data["tweeted"].items():
    for script, tweeted in scripts.items():
        if script == argv[1]:
            if tweeted:
                print(
                    f"Tried to tweet {script} but already tweeted since last data update."
                )
                continue
            else:
                tweeted = True
            print(f"Tweeting {script}...")
            status = "\n".join(
                import_module(".".join(["tweets", tweet_type, script])).tweet(
                    data["pages"]
                )
            )

            print(f"Tweeted: \n{status}")
            api.update_status(status)
            break

open("src/data/status.json", "w").write(dumps(data))
