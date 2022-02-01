"""Tweets the cumulative total of vaccine-related data."""


def tweet(covid_data: dict, population) -> list[str]:
    twelve_plus = (covid_data["COVID-19: Vaccine data"]
                   ["Total Vaccinations 12+"]
                   ["Cumulative total"]
                   )
    five_to_eleven = (covid_data["COVID-19: Vaccine data"]
                      ["Total Vaccinations 5-11"]
                      ["Cumulative total"]
                      )

    # vaccinated = twelve_plus["Second dose"] + five_to_eleven["Second dose"]
    vaccinated = twelve_plus["Second dose"] + 0
    least_one = twelve_plus["First dose"] + five_to_eleven["First dose"]
    boosted = twelve_plus["Boosters"]

    # will change once 5-11 stats update
    total = twelve_plus["Total doses"] + five_to_eleven["First dose"]

    return [
        "💉 TOTALS UPDATE",
        f"(5+) {total:,} doses have now been administered",
        f"(5+) {least_one:,} kiwis have now had at least 1 dose",
        f"(5+) {vaccinated:,} kiwis have now been vaccinated",
        f"(18+) {boosted:,} kiwis have now been boosted",
    ]
