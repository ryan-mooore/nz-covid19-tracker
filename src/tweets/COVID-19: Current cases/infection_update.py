from typing import Union


def tweet(data: dict) -> Union[bool, list[str]]:

    infected = (
        data["COVID-19: Current cases"]["Current situation"]["Change in last 24 hours"][
            "Active"
        ]
        + data["COVID-19: Current cases"]["Current situation"][
            "Change in last 24 hours"
        ]["Recovered"]
        + data["COVID-19: Current cases"]["Current situation"][
            "Change in last 24 hours"
        ]["Deceased"]
    )

    if not infected:
        print("No new active cases in past 24 hours")
        return False

    active = data["COVID-19: Current cases"]["Current situation"]["Total"]["Active"]

    return [
        "🦠 INFECTION UPDATE",
        str(infected)
        + (" people have " if infected > 1 else " person has ")
        + "been infected from COVID-19 in the past 24 hours, bringing the total active cases to "
        + str(active),
    ]
