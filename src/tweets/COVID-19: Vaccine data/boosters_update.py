"""Tweets a graph of booster shots relative to the NZ population."""
from math import ceil, floor


def tweet(covid_data: dict, population) -> list[str]:

    twelve_plus = (covid_data["COVID-19: Vaccine data"]
                   ["Total Vaccinations 12+"]
                   ["Cumulative total"]
                   )

    boosted = twelve_plus["Boosters"]

    ratio = boosted / population.ELIGIBLE.value
    low = floor(ratio * 10) / 10
    high = ceil(ratio * 10) / 10

    boosted_bar_macro = "🟨" * floor((ratio - low) * 100)
    unboosted_bar_macro = "⬛" * ceil((high - ratio) * 100)
    lower_macro = int(low * 100)
    upper_macro = int(high * 100)
    boosted_bar_total = "🟨" * floor(ratio * 10)
    unboosted_bar_total = "⬛" * ceil((1 - ratio) * 10)

    return [
        "💉 BOOSTERS UPDATE",
        f"(18+) New Zealand is now {round(ratio * 100, 2)}% boosted!",
        f"{lower_macro}% {boosted_bar_macro}"
        f"{unboosted_bar_macro} {upper_macro}%",
        f"0% {boosted_bar_total}{unboosted_bar_total} 100%",
    ]
