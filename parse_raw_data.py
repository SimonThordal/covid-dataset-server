#!bash/bin/python

import json
from collections import defaultdict


def f(record):
    return {"date": record['dateRep'], "cases": record['cases']}


if __name__ == "__main__":
    with open("raw_data.json") as fl:
        data = json.load(fl)
    country_dicts = defaultdict(list)
    [country_dicts[record["countryterritoryCode"]].append(f(record)) for record in data['records']]
    for country, records in country_dicts.items():
        with open("api/data/" + country + ".json", "w") as fl:
            json.dump(records, fl)
