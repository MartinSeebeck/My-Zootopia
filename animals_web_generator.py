import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_html(file_name):
  with open (file_name, 'r') as source:
    html_data = source.read()
    return html_data

animals_data = load_data('animals_data.json')
animals_temp = load_html('animals_template.html')


output = ''  # define an empty string
for animal in animals_data:
    # append information to each string
    if 'name' in animal:
        # append information to each string
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        diet = animal.get('characteristics', {}).get('diet')
        if diet:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        locations = animal.get('locations', [])
        if locations:
            output += f"First Location: {locations}<br/>\n"
        animal_type = animal.get('characteristics', {}).get('type')
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"
        output += '</li>'
        print(output)

x = animals_temp.replace("__REPLACE_ANIMALS_INFO__", output)

with open('animals.html', 'w') as dest:
    dest.write(x)

