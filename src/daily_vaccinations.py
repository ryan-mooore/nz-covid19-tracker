from helpers.twitter import data, tweet

NZ_POP = 5122600

fully = data["data"]["vaccines"]["Vaccinations yesterday"]["Second dose administered"]
total = data["data"]["vaccines"]["Vaccinations yesterday"]["Total doses administered"]

tweet(
    [
        f"💉 DAILY VACCINATIONS",
        f"{total} people were given the jab today.",
        f"{fully} more people are now fully vaccinated!",
    ],
    "daily_vaccinations",
)
