
import os
import data_fetcher  # NEU: Importiert unser neues Modul
import json

API_KEY = "LHrqULjJLBkEgZtTymnHWQ==itwvC2zCleVBPWBA"
API_REQ_ANIMALS = "https://api.api-ninjas.com/v1/animals?name="


def load_data(file_path):
  """ Loads a JSON file """
  response = requests.post(file_path, json=data)
  with open('animals_data_2.json', 'w') as dest:
      # write results to json file
      dest.write(response)
  with open('animals_data_2.json', 'r') as handle:
    return json.load(handle)


def load_html(file_name):
    try:
        with open (file_name, 'r') as source:
            html_data = source.read()
            return html_data
    except FileNotFoundError as err:
        print("The HTML template appears to be missing in the home directory.")
        print("Please verify its presence resp. that the file is not being edited in parallel.")
        return


def serialize_animal(animal_obj):
    """
    Changes a single animal object into a formatted HTML string.
    """
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
    else:
        raise KeyError("The data related to 'name' in the online database appears to be missing. Please consult an admin.")
        return
    return output

def main():
    if not API_KEY:
        print("Error: API_KEY not found as a constant.")
        print("Please touch a .env-file in the home directory containing the line: API_KEY=\"IHR_SCHLÜSSEL\"")
        return
    animal = input("Which animal do you want to read about? (use singular in English) ")
    if not animal:
        print("You have not entered an animal name.")
        return
    quarry_animal = animal.capitalize()
    #collect animal data from API
    # --- GEÄNDERT: Ruft die Daten jetzt aus dem data_fetcher-Modul ab ---
    animals_data = data_fetcher.fetch_data(quarry_animal)
    if animals_data is None:
        print("The website data could not be written.")
        return
    animals_temp = load_html('animals_template.html')
    output = ''  # define an empty string
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    #insert req data into html template
    animals_data_insertion_obj = animals_temp.replace("__REPLACE_ANIMALS_INFO__", output)
    with open('animals.html', 'w') as dest:
        #write results to HTML file
        dest.write(animals_data_insertion_obj)
    print("Data retrieval successful.")
    print("Please open the file 'animals.html' in your home folder.")

if __name__ == "__main__":
    main()

