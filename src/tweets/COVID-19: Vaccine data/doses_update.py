from math import floor


def tweet(data: dict) -> list[str]:
    NZ_POP = 5122600

    vaccinations = data["COVID-19: Vaccine data"][
        "COVID-19 vaccinations: daily updates"
    ]["Cumulative total"]

    at_least_one = vaccinations["First dose"]
    vaccinated = vaccinations["Second dose"]

    # "Second dose" gives vaccinated people. Taking this away from "First dose
    # administered" gives people that have had only 1 dose.
    only_one = at_least_one - vaccinated

    tiles = "🟨" * floor(vaccinated / NZ_POP * 25) + "⬜" * floor(only_one / NZ_POP * 25)

    for tile in range(len(tiles), 25):
        tiles += "⬛"

    grid = [tiles[index : index + 5] for index in range(0, len(tiles), 5)]

    return [
        f"💉 DOSES UPDATE",
        f"{round(at_least_one / NZ_POP * 100, 2)}% of people have had at least 1 dose.",
        f"{round(vaccinated / (vaccinated + only_one) * 100, 2)}% of people that have been jabbed are fully vaccinated.",
    ] + grid
