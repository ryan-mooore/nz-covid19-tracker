from json import loads, dumps
from os import environ
from datetime import datetime

import tweepy as tp  # type: ignore

auth = tp.OAuthHandler(environ["CONSUMER_KEY"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["ACCESS_TOKEN"], environ["ACCESS_TOKEN_SECRET"])
api = tp.API(auth)

data = loads(open("src/data/status.json", "r").read())


def tweet(lines: list[str], name: str) -> None:
    status = "\n".join(lines)
    if data["posted"][name]:
        print(
            f"Tried to tweet {name} but no updates to data since {datetime.fromisoformat(data['last_updated']).strftime('%H:%M %d %B')}"
        )
    else:
        data["posted"][name] = True
        open("src/data/status.json", "w").write(dumps(data))
        print("Tweeted: ")
        print('"')
        print(status)
        print('"')
        api.update_status(status)
