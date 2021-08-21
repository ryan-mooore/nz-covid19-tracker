from pymongo import MongoClient  # type: ignore
from os import environ

client = MongoClient(
    host=environ["MONGODB_URI"] if "MONGODB_URI" in environ else "localhost", port=27017
)
db = client.nz_covid_tracker
