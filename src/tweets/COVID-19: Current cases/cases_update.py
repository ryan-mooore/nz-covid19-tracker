def tweet(data: dict) -> list[str]:

    totals = data["pages"]["COVID-19: Current cases"]["Case details"][
        "Total at present"
    ]

    border = (
        totals[
            "People who travelled internationally and were diagnosed in managed facilities at the border"
        ]
        + totals[
            "People in close contact with someone who caught COVID-19 while overseas"
        ]
    )
    community = totals["Caught COVID-19 from someone locally"]
    unknown = (
        totals["Caught COVID-19 within NZ, but source is unknown"]
        + totals["Under investigation"]
    )

    total_str: list[str] = []
    if border:
        total_str.append(f"🛬 From the border: {border}")
    if community:
        total_str.append(
            f"🏡 In the community: {community}",
        )
    if unknown:
        total_str.append(
            f"🔎 Under investigation: {unknown}",
        )

    return [
        "🦠 CASES UPDATE",
        f'There are currently {data["pages"]["COVID-19: Current cases"]["Current situation"]["Total"]["Active"]} active cases of COVID-19 in New Zealand:',
    ] + total_str
