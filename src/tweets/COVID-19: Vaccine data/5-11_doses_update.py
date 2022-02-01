"""Tweets a graph of first and second doses of ages 5-11 relative to the NZ population."""

from math import floor

TOTAL_TILES = 25


def tweet(covid_data: dict, population) -> list[str]:

    five_to_eleven = (covid_data
                      ["COVID-19: Vaccine data"]
                      ["Total Vaccinations 5-11"]
                      ["Cumulative total"]
                      )

    least_one = five_to_eleven["First dose"]
    # vaccinated = five_to_eleven["Second dose"]
    vaccinated = 0

    # "Second dose" gives vaccinated people. Taking this away from "First dose
    # administered" gives people that have had only 1 dose.
    only_one = least_one - vaccinated

    tiles_vaccinated = "🟨" * floor(
        vaccinated / population.FIVE_ELEVEN.value * TOTAL_TILES,
    )
    tiles_first_dose = "⬜" * floor(
        only_one / population.FIVE_ELEVEN.value * TOTAL_TILES,
    )

    tiles = tiles_vaccinated + tiles_first_dose
    tiles += "".join(["⬛" * (TOTAL_TILES - len(tiles))])

    grid = [
        tiles[
            index: index + 5
        ] for index in range(0, len(tiles), 5)
    ]

    return [
        "💉 5-11 DOSES UPDATE",
        f"(5-11) {round(least_one / population.FIVE_ELEVEN.value * 100, 2)}% "
        "of children have had at least 1 dose:",
        f"(5-11) {round(vaccinated / population.FIVE_ELEVEN.value * 100, 2)}% "
        "of children are fully vaccinated",
        f"(5-11) {round(only_one / population.FIVE_ELEVEN.value * 100, 2)}% "
        "of children have only had 1 dose so far",
    ] + grid
