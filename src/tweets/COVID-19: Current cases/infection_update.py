"""Tweets the amount of new infections in the last 24 hours."""
from typing import Union


def tweet(covid_data: dict, population) -> Union[bool, list[str]]:

    infected = (
        (covid_data
         ["COVID-19: Current cases"]
         ["Current situation"]
         ["Change in last 24 hours"]
         ["Active"]
         ) + (covid_data
              ["COVID-19: Current cases"]
              ["Current situation"]
              ["Change in last 24 hours"]
              ["Recovered"]
              ) + (covid_data["COVID-19: Current cases"]
                   ["Current situation"]
                   ["Change in last 24 hours"]
                   ["Deceased"]
                   )
    )

    if not infected:
        print("No new active cases in past 24 hours")
        return False

    active = (covid_data
              ["COVID-19: Current cases"]
              ["Current situation"]
              ["Total"]
              ["Active"]
              )

    conjunction = " people have " if infected > 1 else " person has "

    return [
        "🦠 INFECTION UPDATE",
        str(infected) + conjunction + (
            "been infected from COVID-19 in the past 24 hours, "
            "bringing the total active cases to "
            f"{active:,}"
        ),
    ]
