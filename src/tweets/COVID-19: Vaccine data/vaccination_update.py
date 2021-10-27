"""Tweets a graph of full vaccinations relative to the NZ population."""
from math import ceil, floor


def tweet(covid_data: dict, population) -> list[str]:

    vaccinated = int((
        covid_data
        ["COVID-19: Vaccine data"]
        ["COVID-19 vaccinations: daily updates"]
        ["Cumulative total"]
        ["Second dose"]
    ))
    ratio = vaccinated / population.ELIGIBLE.value
    low = floor(ratio * 10) / 10
    high = ceil(ratio * 10) / 10

    vaccinated_bar_macro = "🟨" * floor((ratio - low) * 100)
    unvaccinated_bar_macro = "⬛" * ceil((high - ratio) * 100)
    macro_lower = int(low * 100)
    macro_lower = int(high * 100)
    vaccinated_bar_total = "🟨" * floor(ratio * 10)
    unvaccinated_bar_total = "⬛" * ceil((1 - ratio) * 10)

    return [
        "💉 VACCINATION UPDATE",
        f"(eligible) New Zealand is now {round(ratio * 100, 2)}% vaccinated!",
        f"{macro_lower}% {vaccinated_bar_macro}"
        f"{unvaccinated_bar_macro} {macro_lower}%",
        f"0% {vaccinated_bar_total}{unvaccinated_bar_total} 100%",
    ]
