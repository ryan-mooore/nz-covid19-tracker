def tweet(data: dict) -> list[str]:

    NZ_POP = 5122600

    fully = data["COVID-19: Vaccine data"]["COVID-19 vaccinations: daily updates"][
        "Vaccinations yesterday"
    ]["Second dose administered"]
    total = data["COVID-19: Vaccine data"]["COVID-19 vaccinations: daily updates"][
        "Vaccinations yesterday"
    ]["Total doses administered"]

    return [
        f"💉 DAILY VACCINATIONS",
        f"{total} people were given the jab today.",
        f"{fully} more people are now fully vaccinated!",
    ]
