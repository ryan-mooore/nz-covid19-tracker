from math import floor, ceil
from re import A


def tweet(data: dict) -> list[str]:
    NZ_POP = 5122600

    vaccinations = data["pages"]["COVID-19: Vaccine data"][
        "COVID-19 vaccinations: daily updates"
    ]["Cumulative total"]

    only_first = vaccinations["First dose administered"]
    any_dose = vaccinations["Total doses administered"]
    vaccinated = vaccinations["Second dose administered"]

    tiles = "🟨" * floor(vaccinated / NZ_POP * 25) + "⬜" * (
        floor(any_dose / NZ_POP * 25) - floor(vaccinated / NZ_POP * 25)
    )

    for tile in range(len(tiles), 25):
        tiles += "⬛"

    grid = [tiles[index : index + 5] for index in range(0, len(tiles), 5)]

    return [
        f"💉 DOSES UPDATE",
        f"{round(any_dose / NZ_POP * 100, 2)}% of people have had at least 1 dose.",
        f"{round(vaccinated / any_dose * 100, 2)}% of people that have been jabbed are fully vaccinated.",
    ] + grid
