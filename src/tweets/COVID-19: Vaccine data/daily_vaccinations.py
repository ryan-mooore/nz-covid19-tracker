"""Tweets the amount of new vaccinations in the last 24 hours."""


def tweet(covid_data: dict, population) -> list[str]:

    vaccinated = (covid_data
                  ["COVID-19: Vaccine data"]
                  ["COVID-19 vaccinations: daily updates"]
                  ["Vaccinations yesterday"]
                  ["Second dose"]
                  )

    any_dose = (covid_data
                ["COVID-19: Vaccine data"]
                ["COVID-19 vaccinations: daily updates"]
                ["Vaccinations yesterday"]
                ["Total doses"]
                )

    return [
        "💉 DAILY VACCINATIONS",
        f"{any_dose} people were given the jab today.",
        f"{vaccinated} more people are now fully vaccinated!",
    ]
