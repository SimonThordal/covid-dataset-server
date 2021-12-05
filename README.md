### Novo Nordisk interview case

The goal of this case is to present a proof of concept for an API that returns a [Eurostat Covid dataset](https://www.ecdc.europa.eu/en/publications-data/data-daily-new-cases-covid-19-eueea-country) in two forms — a rolling endpoint that shows the past 5 days of data for a given country code and an endpoint that returns the total count for each country.

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
For this prototype I am simply storing the data as a JSON file the `data/` folder.

### Output format
For the rolling endpoint I went with the following response format
```
{
	country_code: ES
	case_counts: [[DATE_1, COUNT_1], ..., [DATE_5, COUNT_5]]
}
```
The advantage of the list of tuples is that unlike an object it preserves order, so it can be sorted by date from the backend. I include the country code with the response, even though it is specified by the request. This is potentially superfluous, but means the client won't have to keep track of state.

### Keeping the data up to date

### Testing and monitoring


