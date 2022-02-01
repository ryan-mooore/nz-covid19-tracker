"""Tweets a graph of full vaccinations relative to the NZ population."""
from math import ceil, floor


def tweet(covid_data: dict, population) -> list[str]:

    twelve_plus = (covid_data["COVID-19: Vaccine data"]
                   ["Total Vaccinations 12+"]
                   ["Cumulative total"]
                   )
    five_to_eleven = (covid_data["COVID-19: Vaccine data"]
                      ["Total Vaccinations 5-11"]
                      ["Cumulative total"]
                      )

    # vaccinated = twelve_plus["Second dose"] + five_to_eleven["Second dose"]
    vaccinated = twelve_plus["Second dose"] + 0

    ratio = vaccinated / population.ELIGIBLE.value
    low = floor(ratio * 10) / 10
    high = ceil(ratio * 10) / 10

    vaccinated_bar_macro = "🟨" * floor((ratio - low) * 100)
    unvaccinated_bar_macro = "⬛" * ceil((high - ratio) * 100)
    lower_macro = int(low * 100)
    upper_macro = int(high * 100)
    vaccinated_bar_total = "🟨" * floor(ratio * 10)
    unvaccinated_bar_total = "⬛" * ceil((1 - ratio) * 10)

    return [
        "💉 VACCINATION UPDATE",
        f"(5+) New Zealand is now {round(ratio * 100, 2)}% vaccinated!",
        f"{lower_macro}% {vaccinated_bar_macro}"
        f"{unvaccinated_bar_macro} {upper_macro}%",
        f"0% {vaccinated_bar_total}{unvaccinated_bar_total} 100%",
    ]
