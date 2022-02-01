"""Tweets a summary of active cases and their breakdown."""


def tweet(covid_data: dict, population) -> list[str]:

    locations = (covid_data
                 ["COVID-19: Current cases"]
                 ["Location of active cases"]
                 ["Total at present"]
                 )

    self_isolation = locations["Self Isolation"]
    managed_isolation = locations["Managed Isolation"]
    hospital = locations["Hospital"]
    other = locations["New Case Processing"] + locations["Other"]
    total = self_isolation + managed_isolation + hospital + other

    total_str: list[str] = []
    if self_isolation:
        total_str.append(f"🏠 Undergoing self-isolation: {self_isolation:,}")
    if managed_isolation:
        total_str.append(
            f"🏨 Under managed isolation: {managed_isolation:,}",
        )
    if hospital:
        total_str.append(
            f"🏥 In hospital: {hospital:,}",
        )
    if other:
        total_str.append(
            f"❓ Unknown/other: {other:,}",
        )

    return [
        "🦠 ISOLATION UPDATE",
        f"There are currently {total:,} people isolating due to "
        "COVID-19 in New Zealand: ",
    ] + total_str
