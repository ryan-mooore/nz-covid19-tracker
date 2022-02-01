"""Tweets a summary of active cases and their breakdown."""


def tweet(covid_data: dict, population) -> list[str]:

    totals = (covid_data
              ["COVID-19: Current cases"]
              ["Source of active cases"]
              ["Total at present"]
              )

    border = (
        totals[
            "People who travelled internationally and were diagnosed "
            "in managed facilities at the border"
        ] + totals[
            "People in close contact with someone who "
            "caught COVID-19 while overseas"
        ]
    )
    community = totals["Caught COVID-19 from someone locally"]
    unknown = (
        totals[
            "Caught COVID-19 within NZ, but source is unknown"
        ] + totals[
            "Under investigation"
        ])

    total_str: list[str] = []
    if border:
        total_str.append(f"🛬 From the border: {border:,}")
    if community:
        total_str.append(
            f"🏡 In the community: {community:,}",
        )
    if unknown:
        total_str.append(
            f"🔎 Under investigation: {unknown:,}",
        )

    active = (covid_data
              ["COVID-19: Current cases"]
              ["Number of active cases"]
              ["Total at present"]
              ["Confirmed"]
              )

    return [
        "🦠 CASES UPDATE",
        f"There are currently {active:,} active cases "
        "of COVID-19 in New Zealand: ",
    ] + total_str
