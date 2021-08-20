from math import ceil, floor

from helpers.twitter import data, tweet

NZ_POP = 5122600
vaccinated = int(
    data["data"]["vaccines"]["Cumulative total"]["Second dose administered"]
)
ratio = vaccinated / NZ_POP
low = floor(ratio * 10) / 10
high = ceil(ratio * 10) / 10

tweet(
    [
        f"💉 VACCINATION UPDATE",
        f"New Zealand is now {round(ratio * 100, 2)}% vaccinated!",
        f"{int(low * 100)}% {'🟨' * floor((ratio - low) * 100)}{'⬛' * ceil((high - ratio) * 100)} {int(high * 100)}%",
        f"0% {'🟨' * floor(ratio * 10)}{'⬛' * ceil((1 - ratio) * 10)} 100%",
    ],
    "vaccination_update",
)
