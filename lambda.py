# Dicrionaries and sorting data by using lambda function
people = [
    {"name": "Nabeel", "house": "London" },
    {"name": "Aqeel", "house": "New York" },
    {"name": "Israr", "house": "Washington DC" },
    {"name": "Shahroz", "house": "Barmhingham" },
    
]

people.sort(key=lambda person: person["name"])

print(people)