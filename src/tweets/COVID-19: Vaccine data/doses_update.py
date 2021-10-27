"""Tweets a graph of first and second doses relative to the NZ population."""

from math import floor

TOTAL_TILES = 25


def tweet(covid_data: dict, population) -> list[str]:

    vaccinations = (covid_data
                    ["COVID-19: Vaccine data"]
                    ["COVID-19 vaccinations: daily updates"]
                    ["Cumulative total"]
                    )

    least_one = vaccinations["First dose"]
    vaccinated = vaccinations["Second dose"]

    # "Second dose" gives vaccinated people. Taking this away from "First dose
    # administered" gives people that have had only 1 dose.
    only_one = least_one - vaccinated

    tiles_vaccinated = "🟨" * floor(
        vaccinated / population.ELIGIBLE.value * TOTAL_TILES,
    )
    tiles_first_dose = "⬜" * floor(
        only_one / population.ELIGIBLE.value * TOTAL_TILES,
    )

    tiles = tiles_vaccinated + tiles_first_dose
    tiles += "".join(["⬛" * (TOTAL_TILES - len(tiles))])

    grid = [
        tiles[
            index: index + 5
        ] for index in range(0, len(tiles), 5)
    ]

    return [
        "💉 DOSES UPDATE",
        f"(eligible) {round(least_one / population.ELIGIBLE.value * 100, 2)}% "
        "of people have had at least 1 dose",
        f"(eligible) {round(only_one / population.ELIGIBLE.value * 100, 2)}% "
        "of people have had only 1 dose",
    ] + grid
