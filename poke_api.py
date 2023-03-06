import requests

def get_pokemon_info(name):
    """
    Getting information for a Pokémon from the site called PokéAPI.

    Parameters:
    name (str or int): The name of the Pokémon to get.

    Returns:
    dict: A dictionary which contains all the information we got from the site PokéAPI , if retrieved successfully.
    None: If the Pokémon information we dont get successfully.

    Prints a summary of actions which was performed.
    """
    name = str(name).strip().lower()

    # Convert parameter to string and format URL
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

    # Make an API request
    response = requests.get(url)

    # Checking for a successful response
    if response.ok:
        return response
    else:
        print(f"Failed fetching the information for POKEMON {name}")

        return None

        # Getting information for Giratina
Giratina_info = get_pokemon_info("Giratina")
print(Giratina_info)

# information for Pumpkaboo
Pumpkaboo_info = get_pokemon_info("Pumpkaboo")
print(Pumpkaboo_info)


