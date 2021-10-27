"""Interface for MongoDB database."""
from os import environ

from pymongo import MongoClient  # type: ignore

MONGODB_PORT = 27017

client = MongoClient(
    host=environ["MONGODB_URI"] if "MONGODB_URI" in environ else "localhost",
    port=MONGODB_PORT,
)
db = client.nz_covid_tracker
