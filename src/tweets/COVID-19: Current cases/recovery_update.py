from typing import Union


def tweet(data: dict) -> Union[bool, list[str]]:
    if not data["COVID-19: Current cases"]["Current situation"][
        "Change in last 24 hours"
    ]["Recovered"]:
        print("No recovered cases in past 24 hours")
        return False

    totals = data["COVID-19: Current cases"]["Case details"]["Change in last 24 hours"]

    total_str: list[str] = []
    if (
        totals[
            "People who travelled internationally and were diagnosed in managed facilities at the border"
        ]
        + totals[
            "People in close contact with someone who caught COVID-19 while overseas"
        ]
        < 0
    ):
        total_str.append(
            f'🛬 From the border: -{totals["People who travelled internationally and were diagnosed in managed facilities at the border"] + totals["People in close contact with someone who caught COVID-19 while overseas"]}'
        )
    if totals["Caught COVID-19 from someone locally"] < 0:
        total_str.append(
            f'🏡 From the community: -{totals["Caught COVID-19 from someone locally"]}',
        )
    if (
        totals["Caught COVID-19 within NZ, but source is unknown"]
        + totals["Under investigation"]
        < 0
    ):
        total_str.append(
            f'🔎 Under investigation: -{totals["Caught COVID-19 within NZ, but source is unknown"] + totals["Under investigation"]}'
        )

    return [
        "🦠 RECOVERY UPDATE",
        str(
            data["COVID-19: Current cases"]["Current situation"][
                "Change in last 24 hours"
            ]["Recovered"]
        )
        + " people have recovered from COVID-19 in the past 24 hours, bringing the total active cases to "
        + str(data["COVID-19: Current cases"]["Current situation"]["Total"]["Active"])
        + ":",
    ]
