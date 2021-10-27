"""Tweets the cumulative total of vaccine-related data."""


def tweet(covid_data: dict, population) -> list[str]:
    vaccinations = (covid_data
                    ["COVID-19: Vaccine data"]
                    ["COVID-19 vaccinations: daily updates"]
                    ["Cumulative total"]
                    )

    least_one = vaccinations["First dose"]
    vaccinated = vaccinations["Second dose"]
    total = vaccinations["Total doses"]

    return [
        "💉 TOTALS UPDATE",
        f"{vaccinated:,} kiwis have now been fully vaccinated",
        f"{least_one:,} kiwis have now had at least 1 dose",
        f"{total:,} doses have now been administered",
    ]
