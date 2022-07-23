import os

APP_MONGO_DB = os.getenv("APP_MONGO_DB", "granja")
APP_MONGO_URI = os.getenv("APP_MONGO_URI", "mongodb://user:pass@localhost/?retryWrites=true&w=majority")
