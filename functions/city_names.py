def city_country(city, country):
    new_city = f"{city}, {country}"
    return new_city

cities = []
cities.append(city_country("Medellin", "Colombia"))
cities.append(city_country("Buenos Aires", "Argentina"))
cities.append(city_country("Porto Allegre", "Brasil"))

for city in cities:
    print(city)
