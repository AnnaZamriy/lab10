countries = {
    "Ukraine": 603628,
    "France": 551695,
    "Spain": 505990,
    "Sweden": 450295,
    "Germany": 357022,
    "Finland": 338424,
    "Norway": 323802 }

with open("countries.txt", "w") as c_file:
    for country in countries.keys():
        c_file.write(country + "\n")

with open("squares.txt", "w") as sq_file:
    for square in countries.values():
        sq_file.write(str(square) + "\n")

c_max = max(countries, key=countries.get)
area_max = countries[c_max]

with open("largest.txt", "w") as max_file:
    max_file.write(c_max + ": " + str(area_max))
