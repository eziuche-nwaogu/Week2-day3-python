# The code beow has been modified to output the individual states and their cities using a for loop
# create a mapping of state to abbreviation
states = {
    "Abia": "AB",
    "Adamawa": "AD",
    "Akwa Ibom": "AKW",
    "Benue": "BEN",
    "Enugu": "EN",
}

# create a basic set of states and some cities in them
cities = {"AB": "Aba", "AD": "Yola", "AKW": "Uyo", "BEN": "Benue", "EN": "New Haven"}

# add some more cities
cities["KN"] = "Kano"
cities["KD"] = "Kaduna"

# print out some cities
print("-" * 10)
my_states = list(states.keys())
print(my_states)
my_cities = list(cities.values())
print(my_cities)
print("AB State has: ", cities["AB"])
print("EN State has: ", cities["EN"])
print("-" * 10)
print(f"{my_states[0]} state has: {my_cities[0]}")

# print states and cities
print("-" * 10)
for state, city_code in states.items():
    print(f"{state} state has {cities[city_code]}")

# print some states
print("-" * 10)
print("Abia's abbreviation is: ", states["Abia"])
print("Enugu's abbreviation is: ", states["Enugu"])
# do it by using the state then cities dict
print("-" * 10)
print("Adamawa has: ", cities[states["Adamawa"]])
print("Benue has: ", cities[states["Benue"]])
# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
print(f"and has city {cities[abbrev]}")
print("-" * 10)
53  # safely get a abbreviation by state that might not be there
state = states.get("Texas")
if not state:
    print("Sorry, no Texas.")
# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")
