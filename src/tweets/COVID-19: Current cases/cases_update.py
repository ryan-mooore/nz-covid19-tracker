def tweet(data: dict) -> list[str]:

    totals = data["COVID-19: Current cases"]["Case details"]["Total at present"]

    total_str: list[str] = []
    if (
        totals[
            "People who travelled internationally and were diagnosed in managed facilities at the border"
        ]
        + totals[
            "People in close contact with someone who caught COVID-19 while overseas"
        ]
    ):
        total_str.append(
            f'🛬 From the border: {totals["People who travelled internationally and were diagnosed in managed facilities at the border"] + totals["People in close contact with someone who caught COVID-19 while overseas"]}'
        )
    if totals["Caught COVID-19 from someone locally"]:
        total_str.append(
            f'🏡 From the community: {totals["Caught COVID-19 from someone locally"]}',
        )
    if (
        totals["Caught COVID-19 within NZ, but source is unknown"]
        + totals["Under investigation"]
    ):
        f'🔎 Under investigation: {totals["Caught COVID-19 within NZ, but source is unknown"] + totals["Under investigation"]}',

    return [
        "🦠 CASES UPDATE",
        f'There are currently {data["COVID-19: Current cases"]["Current situation"]["Total"]["Active"]} active cases of COVID-19 in New Zealand:',
    ] + total_str
