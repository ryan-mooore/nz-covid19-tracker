from typing import Union


def tweet(data: dict) -> Union[bool, list[str]]:

    recovered = data["pages"]["COVID-19: Current cases"]["Current situation"][
        "Change in last 24 hours"
    ]["Recovered"]

    if not recovered:
        print("No new active cases in past 24 hours")
        return False

    active = data["pages"]["COVID-19: Current cases"]["Current situation"]["Total"][
        "Active"
    ]

    return [
        "🦠 RECOVERY UPDATE",
        str(recovered)
        + (" people have " if recovered > 1 else " person has ")
        + "been infected from COVID-19 in the past 24 hours, bringing the total active cases to "
        + str(active),
    ]

    if border + community + unknown == recovered:
        return [
            "🦠 RECOVERY UPDATE",
            str(recovered)
            + (" people have " if recovered > 1 else " person has ")
            + "recovered from COVID-19 in the past 24 hours, bringing the total active cases to "
            + str(active)
            + ":",
        ] + total_str
    else:
        print("Error: recovery number did not equal current - history")
        return False
