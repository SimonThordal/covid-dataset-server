import hug

@hug.get("/hello_world")
def hello_world():
	return "hello world"

@hug.get("/rolling-five-days/{countryterritoryCode}")
def rolling_five_days():
	return []