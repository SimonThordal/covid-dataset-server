import hug
import json
from pathlib import Path
import os
import datetime

# Given a list where the first member is a datestring as "13/04/1983"
# returns the same list with the first member cast to a datetime
def parse_date(date: str) -> list:
    date_format = '%d/%m/%Y'
    return datetime.strptime(date, date_format)


def load_counts(country_code: str) -> list:
    datapath = Path(os.path.abspath(os.path.dirname(__file__))) / "data"
    filename = Path(country_code).with_suffix(".json")
    path = datapath / filename
    with path.open() as fl:
        return json.load(fl)


@hug.get("/hello_world")
def hello_world():
    return "hello world"


@hug.get("/rolling-five-days/{countryterritoryCode}")
def rolling_five_days(countryterritoryCode: hug.types.text):
    countryterritoryCode = countryterritoryCode.lower()
    data = dict()
    dates_counts = load_counts(countryterritoryCode)
    data['counts'] = sort(dates_counts, key=parse_date)[-5:]
    data['country_code'] = countryterritoryCode
    return data
