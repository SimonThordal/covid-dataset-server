import hug
import json
from pathlib import Path
from os.path import abspath, dirname, isfile
from os import listdir
from datetime import datetime

datapath = Path(abspath(dirname(__file__))) / "data"

# Given a list where the first member is a datestring as "13/04/1983"
# returns the same list with the first member cast to a datetime
def parse_date(date_count: str) -> list:
    date_format = '%d/%m/%Y'
    return datetime.strptime(date_count[0], date_format)


def get_country_codes_from_files() -> list:
    return [entry.stem for entry in datapath.iterdir() if entry.is_file()]


def load_counts(country_code: str) -> list:
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
    data['counts'] = sorted(dates_counts, key=parse_date)[-5:]
    data['country_code'] = countryterritoryCode
    return data

@hug.get('/total-data')
def totals_per_country():
    country_codes = get_country_codes_from_files()
    return {code: sum([count for _, count in load_counts(code)]) for code in country_codes}