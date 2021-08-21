from json import loads, dumps
from os import environ
from datetime import datetime
from sys import argv
from typing import Type
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
                break
            else:
                data["tweeted"][tweet_type][script] = True
            print(f"Tweeting {script}...")
            try:
                status = "\n".join(
                    import_module(".".join(["tweets", tweet_type, script])).tweet(
                        data["pages"]
                    )
                )
            except TypeError:
                print(f"Aborted tweeting {script}...")
                break

            print(f"Tweeted: \n{status}")
            api.update_status(status)
            break
    else:
        continue
    break
else:
    print(f"Tweet {argv[1]} could not be found in status.json")

open("src/data/status.json", "w").write(dumps(data))
