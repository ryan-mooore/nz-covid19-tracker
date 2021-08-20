from helpers.twitter import data, tweet
from math import floor, ceil

NZ_POP = 5122600

only_first = data["data"]["vaccines"]["Cumulative total"]["First dose administered"]
any_dose = data["data"]["vaccines"]["Cumulative total"]["Total doses administered"]
vaccinated = data["data"]["vaccines"]["Cumulative total"]["Second dose administered"]

tiles = "🟨" * floor(vaccinated / NZ_POP * 25) + "⬜" * (
    floor(any_dose / NZ_POP * 25) - floor(vaccinated / NZ_POP * 25)
)

for tile in range(len(tiles), 25):
    tiles += "⬛"

grid = [tiles[index : index + 5] for index in range(0, len(tiles), 5)]

tweet(
    [
        f"💉 DOSES UPDATE",
        f"{round(any_dose / NZ_POP * 100, 2)}% of people have had at least 1 dose.",
        f"{round(vaccinated / only_first * 100, 2)}% of people that have been jabbed are fully vaccinated.",
    ]
    + grid,
    "doses_update",
)
