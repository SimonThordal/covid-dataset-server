import hug
import json
from pathlib import Path
import os

def load_counts(country_code: str) -> list:
    datapath = Path(os.path.abspath(os.path.dirname(__file__))) / "data"
    filename = Path(country_code).with_suffix(".json")
    path = datapath / filename
    with path.open() as fl:
        return json.load(fl)


def get_country(country_code: str) -> str:
    pass


@hug.get("/hello_world")
def hello_world():
    return "hello world"


@hug.get("/rolling-five-days/{countryterritoryCode}")
def rolling_five_days(countryterritoryCode: hug.types.text):
    data = dict();
    data['counts'] = load_counts(countryterritoryCode)
    data['country_code'] = countryterritoryCode
    data['country'] = get_country(countryterritoryCode)
    return data
