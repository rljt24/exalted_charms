import json
import pprint

counts = {}

file = open('test.json', encoding="utf8")

data = json.load(file)

for charm in data:
    if charm['Type of Exalt'] == 'Solar':
        if charm['Abilities'] in counts.keys():
            counts[charm['Abilities']] += 1
        else:
            counts.update({charm['Abilities']: 1})

pprint.pprint(counts)

file.close()
