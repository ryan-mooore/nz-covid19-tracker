from typing import Union


def tweet(data: dict) -> Union[bool, list[str]]:
    if not data["pages"]["COVID-19: Current cases"]["Current situation"][
        "Change in last 24 hours"
    ]["Recovered"]:
        print("No recovered cases in past 24 hours")
        return False

    history = data["history"]["COVID-19: Current cases"]["Case details"][
        "Change in last 24 hours"
    ]
    current = data["pages"]["COVID-19: Current cases"]["Case details"][
        "Change in last 24 hours"
    ]
    recovered = data["pages"]["COVID-19: Current cases"]["Current situation"][
        "Change in last 24 hours"
    ]["Recovered"]
    active = data["pages"]["COVID-19: Current cases"]["Current situation"]["Total"][
        "Active"
    ]

    def compare(keys: Union[str, list[str]]) -> int:
        if type(keys) is str:
            keys = [keys]
        total = 0
        for key in keys:
            total += current[key] - history[key]
        return total

    border = compare(
        [
            "People who travelled internationally and were diagnosed in managed facilities at the border",
            "People in close contact with someone who caught COVID-19 while overseas",
        ]
    )
    community = compare("Caught COVID-19 from someone locally")
    unknown = compare(
        ["Caught COVID-19 within NZ, but source is unknown", "Under investigation"]
    )

    total_str: list[str] = []
    if border < 0:
        total_str.append(f"🛬 From the border: {border}")
    if community < 0:
        total_str.append(
            f"🏡 In the community: {community}",
        )
    if unknown < 0:
        total_str.append(
            f'🔎 Under investigation: -{current["Caught COVID-19 within NZ, but source is unknown"] + current["Under investigation"]}'
        )
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
