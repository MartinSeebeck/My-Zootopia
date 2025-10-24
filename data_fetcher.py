import os
import requests
from dotenv import load_dotenv

# Loads env variable from the .env-file.
# This script checks for a .env-file in the base directory.
load_dotenv()

def fetch_data(animal_name):
  """
  Picks animal names for variable 'animal_name' from API-Ninjas API.
  """
  # Gets API key from the env variable.
  # os.environ.get() is the method to access same.
  api_key = os.environ.get("API_KEY")

  if not api_key:
      print("Fehler: API_KEY not found in .env-file or file missing.")
      print("Please touch an .env file with the contents: API_KEY=\"IHR_SCHLÜSSEL\"")
      return None

  api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  headers = {"X-Api-Key": api_key}

  try:
      response = requests.get(api_url, headers=headers)
      response.raise_for_status()
      return response.json()
  except requests.exceptions.RequestException as e:
      print(f"Error checking API: {e}")
      if 'response' in locals() and response is not None:
          print(f"Server-Antwort: {response.text}")
      return None





