### Novo Nordisk interview case

The goal of this case is to present a proof of concept for an API that returns a [Eurostat Covid dataset](https://www.ecdc.europa.eu/en/publications-data/data-daily-new-cases-covid-19-eueea-country) in two forms — a rolling endpoint that shows the past 5 days of data for a given country code and an endpoint that returns the total count for each country.

### Choice of framework

Since this is a proof of concept I will base my choice of framework for being
1. Easy to install. The less that needs to be done to set it up, the better
4. Testing tools should be readily available
2. The framework should be lightweight and robust.
3. Prototyping should be fast
5. Easily documentable

Python comes with many platforms and it is otherwise quick to install, ticking box 1. I have experience with `Hug` which is a lightweight framework for API development with a self-documenting API that checks box 3-5. It does not come with a large ecosystem, but my assumption is that if we were to expand on this then the the choice of framework would depend on the requirements to the app.
  
### Storage

### Keeping the data up to date

### Testing and monitoring


