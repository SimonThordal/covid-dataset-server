## API showcase

The goal of this case is to present a proof of concept for an API that returns a [Eurostat Covid dataset](https://www.ecdc.europa.eu/en/publications-data/data-daily-new-cases-covid-19-eueea-country) in two forms — a rolling endpoint that shows the past 5 days of data for a given country code and an endpoint that returns the total count for each country.

## Requirements and installation
You will need Make sure you have Python 3.8 or greater installed along wth `pip` or `pipenv`. To install dependencies run either `pip install -r requirements.txt` or `pipenv install`. You can now start the server using either `hug -f api/api.py` or `pipenv run hug -f api/api.py`.

The server should now be available at [http://localhost:8000](http://localhost:8000) which is also where you will the documentation for the API endpoints.


## Implementation and considerations
### Assumptions
I am assuming that this is the backend of something that will either stay a microservice, perhaps backing a visualization, or a proof of concept that will be developed into something larger later. 
I am also assuming that we are only interested in the case data at the moment, not the deaths.

### Choice of framework

Since this is a proof of concept I will base my choice of framework for being
1. Easy to install. The less that needs to be done to set it up, the better
4. Testing tools should be readily available
2. The framework should be lightweight and robust.
3. Prototyping should be fast
5. Easily documentable

Python comes with many platforms and it is otherwise quick to install, ticking box 1. I have experience with `Hug` which is a lightweight framework for API development with a self-documenting API that checks box 3-5.

Since I am assuming that this stays a microservice I do not care much about an ecosystem of packages, an ORM and so on. If this would be used for more than a POC then choosing the framework would also need to take future features and scaling into account.
  
### Storage
For this prototype I am simply storing the data as JSON files the `data/` folder, one for each country with the country code as name. To avoid having to parse the data on every request I only store the information that is actually needed for API—the dates and the infection count—and I store it in the same way that we want to serve it from the API.


### Output format
For the rolling endpoint I went with the following response format
```
{
	country_code: ESP
	case_counts: [[DATE_1, COUNT_1], ..., [DATE_5, COUNT_5]]
}
```
The advantage of the list of tuples is that unlike an object it preserves order, so it can be sorted by date from the backend. I include the country code with the response, even though it is specified by the request. This is potentially superfluous, but means the client won't have to keep track of state.

For the totals endpoint an object with the country code as key and the totals as value is used,
```
{
	ESP: 10000,
	DNK: 1000,
	...
}
```

## Future work

### Implementing a database
While files work fine for now, additional functionality would quickly result in a complex storage system that would be hard to maintain. As for what database to choose from I would prioritize familiarity over features and go for a SQL database to avoid developers having to learn a new query language.  

### Keeping the data up to date
To turn the source data into the lists of lists that I am using `parse_raw_data.py` which grabs the relevant data from `raw_data.json` and places it in the `api/data` folder, ready to be served.
If we wanted to keep this up to data we could fetch a new version of `raw_data.json` either through the command line or with a script. Running `parse_raw_data.py` again would then update the data served through the API. Both of these could be scheduled using a cronjob to run a couple of times per day.

### Testing and monitoring
A bit of testing has already been added using `unittest`, mainly for development purposes. Was this to go live with a continuously updated dataset, then monitoring the source data would be important to avoid that we weren't suddenly missing data or getting data in a format we cannot parse. This could be anything from a third party service like [Bugsnag](https://www.bugsnag.com/) or [Papertrail](https://papertrailapp.com/) to email or slack alerts on exceptions.
