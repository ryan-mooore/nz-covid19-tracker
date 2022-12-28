NOTE: As of the end of 2022, this repository has been archived due to Heroku no longer supporting free dynos, as well as NZ returning to normality.

# nz-covid19-tracker
[nz-covid-tracker](https://twitter.com/covid19_nz) is a Twitter bot tweeting updates to both COVID-19 vaccination and cases status in New Zealand. It operates using a couple of simple python scripts and a mongoDB database. The database simply stores the last data and date update on the website to check whether new data has been posted or not.

## Tweets
There are a total of 6 different status updates the bot can post, which can be found under [src/tweets](src/tweets) - 3 cases update tweets and 3 vaccination update tweets. The bot attempts to tweet each of these 1 once a day between 10AM and 8PM in 2 hour intervals. If the data has not been updated the status update will be skipped for the day.
## Scraping
A seperate [scraping script](/src/scrape.py) checks the [health.govt.nz](https://www.health.govt.nz/) website every hour for potential data updates and scrapes the website if there is new data, although the data is only typically updated between 1pm and 2pm.
# Info
The bot should be up and running on Twitter [@covid19_nz](https://twitter.com/covid19_nz).
