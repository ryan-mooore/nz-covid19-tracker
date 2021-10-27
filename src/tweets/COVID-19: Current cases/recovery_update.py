"""Tweets the amount of new recoveries in the last 24 hours."""
from typing import Union


def tweet(covid_data: dict, population) -> Union[bool, list[str]]:

    recovered = (covid_data
                 ["COVID-19: Current cases"]
                 ["Current situation"]
                 ["Change in last 24 hours"]
                 ["Recovered"]
                 )

    if not recovered:
        print("No new active cases in past 24 hours")
        return False

    active = (covid_data
              ["COVID-19: Current cases"]
              ["Current situation"]
              ["Total"]
              ["Active"]
              )

    conjunction = " people have " if recovered > 1 else " person has "

    return [
        "🦠 RECOVERY UPDATE",
        str(recovered) + conjunction + (
            "recovered from COVID-19 in the past 24 hours, "
            "bringing the total active cases to "
            f"{active:,}"
        ),
    ]
