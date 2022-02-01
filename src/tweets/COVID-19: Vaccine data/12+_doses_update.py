"""Tweets a graph of first and second doses of ages 12+ relative to the NZ population."""

from math import floor

TOTAL_TILES = 25


def tweet(covid_data: dict, population) -> list[str]:

    twelve_plus = (covid_data
                   ["COVID-19: Vaccine data"]
                   ["Total Vaccinations 12+"]
                   ["Cumulative total"]
                   )

    least_one = twelve_plus["First dose"]
    vaccinated = twelve_plus["Second dose"]

    # "Second dose" gives vaccinated people. Taking this away from "First dose
    # administered" gives people that have had only 1 dose.
    only_one = least_one - vaccinated

    tiles_vaccinated = "🟨" * floor(
        vaccinated / population.TWELVE_PLUS.value * TOTAL_TILES,
    )
    tiles_first_dose = "⬜" * floor(
        only_one / population.TWELVE_PLUS.value * TOTAL_TILES,
    )

    tiles = tiles_vaccinated + tiles_first_dose
    tiles += "".join(["⬛" * (TOTAL_TILES - len(tiles))])

    grid = [
        tiles[
            index: index + 5
        ] for index in range(0, len(tiles), 5)
    ]

    return [
        "💉 12+ DOSES UPDATE",
        f"(12+) {round(least_one / population.TWELVE_PLUS.value * 100, 2)}% "
        "of people have had at least 1 dose:",
        f"(12+) {round(vaccinated / population.TWELVE_PLUS.value * 100, 2)}% "
        "of people are fully vaccinated",
        f"(12+) {round(only_one / population.TWELVE_PLUS.value * 100, 2)}% "
        "of people have only had 1 dose so far",
    ] + grid
