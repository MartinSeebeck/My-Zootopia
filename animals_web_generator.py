import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_html(file_name):
  with open (file_name, 'r') as source:
    html_data = source.read()
    return html_data

def serialize_animal(animal_obj):
    output = ''
    # append information to each string
    if 'name' in animal_obj:
        # append information to each string
        output += '<li class="cards__item">'
        output += f'<div class="card__title"><font color=#FF0000>{animal_obj['name']}</font></div><p class="card__text">'
        tax = animal_obj.get('taxonomy', {}).get('scientific_name')
        if tax:
            output += f"<strong>Species designation:</strong> <em>{animal_obj['taxonomy']['scientific_name']}</em><br/>\n"
        animal_type = animal_obj.get('characteristics', {}).get('type')
        if animal_type:
            output += f"<strong>Type:</strong> {animal_type}<br/>\n"
        diet = animal_obj.get('characteristics', {}).get('diet')
        if diet:
            output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
        threat = animal_obj.get('characteristics', {}).get('biggest_threat')
        if threat:
            output += f"<strong>Threatened by:</strong> {animal_obj['characteristics']['biggest_threat']}<br/>\n"
        lifespan = animal_obj.get('characteristics', {}).get('lifespan')
        if lifespan:
            output += f"<strong>Lifespan:</strong> {animal_obj['characteristics']['lifespan']}<br/>\n"
        locations = animal_obj.get('locations', [])
        if locations:
            delimiter = ", "
            str_from_list = delimiter.join(locations)
            output += f"<strong>Spotted in:</strong> {str_from_list}<br/>\n"
        output += '</p></li>'
    return output


animals_data = load_data('animals_data.json')
animals_temp = load_html('animals_template.html')


output = ''  # define an empty string
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)


x = animals_temp.replace("__REPLACE_ANIMALS_INFO__", output)

with open('animals.html', 'w') as dest:
    dest.write(x)
