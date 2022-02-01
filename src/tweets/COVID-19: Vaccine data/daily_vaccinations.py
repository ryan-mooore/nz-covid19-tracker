"""Tweets the amount of new vaccinations in the last 24 hours."""


def tweet(covid_data: dict, population) -> list[str]:

    twelve_plus = (covid_data["COVID-19: Vaccine data"]
                   ["Total Vaccinations 12+"]
                   ["Vaccinations yesterday"]
                   )
    five_to_eleven = (covid_data["COVID-19: Vaccine data"]
                      ["Total Vaccinations 5-11"]
                      ["Vaccinations yesterday"]
                      )

    # I am aware of third doses however for simplicity's sake
    # second doses are counted as fully vaccinated as
    # there is to no way to tell whether any one second dose
    # represents a full vaccination or not.
    # vaccinated = twelve_plus["Second dose"] + five_to_eleven["Second dose"]
    vaccinated = twelve_plus["Second dose"] + 0
    any_dose = twelve_plus["Total doses"] + five_to_eleven["First dose"]
    boosted = twelve_plus["Boosters"]

    return [
        "💉 DAILY VACCINATIONS",
        f"(5+) {any_dose:,} people were given the jab today.",
        f"(5+) {vaccinated:,} more people are now vaccinated!",
        f"(18+) {boosted:,} more people got booster shots!",
    ]
