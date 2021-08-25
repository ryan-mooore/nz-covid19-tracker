def tweet(data: dict) -> list[str]:

    NZ_POP = 5122600

    vaccinated = data["COVID-19: Vaccine data"]["COVID-19 vaccinations: daily updates"][
        "Vaccinations yesterday"
    ]["Second dose administered"]
    any_dose = data["COVID-19: Vaccine data"]["COVID-19 vaccinations: daily updates"][
        "Vaccinations yesterday"
    ]["Total doses administered"]

    return [
        f"💉 DAILY VACCINATIONS",
        f"{any_dose} people were given the jab today.",
        f"{vaccinated} more people are now fully vaccinated!",
    ]
