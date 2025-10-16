import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
  if 'name' in animal:
    print(f"Name: {animal['name']}")
    diet = animal.get('characteristics', {}).get('diet')
    if diet:
      print(f"Diet: {diet}")
    locations = animal.get('locations', [])
    if locations:
      print(f"First Location: {locations[0]}")
    animal_type = animal.get('characteristics', {}).get('type')
    if animal_type:
      print(f"Type: {animal_type}")
    print('-*' * 25)
