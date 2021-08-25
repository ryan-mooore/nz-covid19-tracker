from typing import Union


def tweet(data: dict) -> Union[bool, list[str]]:

    recovered = data["COVID-19: Current cases"]["Current situation"][
        "Change in last 24 hours"
    ]["Recovered"]

    if not recovered:
        print("No new active cases in past 24 hours")
        return False

    active = data["COVID-19: Current cases"]["Current situation"]["Total"]["Active"]

    return [
        "🦠 RECOVERY UPDATE",
        str(recovered)
        + (" people have " if recovered > 1 else " person has ")
        + "recovered from COVID-19 in the past 24 hours, bringing the total active cases to "
        + str(active),
    ]
