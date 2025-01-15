import json
import webbrowser
import re

def search_animes(data, input_value, song_type_filter=None, type_number_filter=None):
    """
    Searches the JSON data for partial matches across specified fields.
    
    Parameters:
        data (list): List of anime data.
        input_value (str): The input value to match.
        song_type_filter (int): Filter by songType (1 for OP, 2 for ED, 3 for INS).
        type_number_filter (int): Filter by typeNumber.
    
    Returns:
        list: List of tuples with matching anime and the field it matched on.
    """
    fields_to_search = ["animeEnglishName", "animeRomajiName", "songArtist", "songName"]
    results = []

    for anime in data:
        for field in fields_to_search:
            anime_field = anime.get(field, "")
            anime_field_clean = re.sub('[^a-zA-Z\d\s]+', ' ', anime_field)
            if input_value.lower() in anime_field_clean.lower() or input_value.lower() in anime_field.lower():
                # Apply additional filters if specified
                if song_type_filter is not None and anime['songType'] != song_type_filter:
                    continue
                if type_number_filter is not None and anime['typeNumber'] != type_number_filter:
                    continue
                results.append((anime, field))
                break  # Stop checking other fields once a match is found for this anime

    return results



def parse_input(search_input):
    """
    Parses the input to extract potential songType and typeNumber filters.
    
    Parameters:
        search_input (str): The user's input string.
    
    Returns:
        tuple: (cleaned_input, song_type_filter, type_number_filter)
    """
    match = re.search(r'(.*?)(\s+)(op|ed|ins)(\d*)$', search_input, re.IGNORECASE)
    if match:
        base_name = match.group(1) + match.group(2)  # Preserve spaces before the song type
        base_name = base_name[:len(base_name)-1]
        song_type = match.group(3).lower()
        type_number = int(match.group(4)) if match.group(4).isdigit() else None
        # Map song type to songType integer
        song_type_map = {'op': 1, 'ed': 2, 'ins': 3}
        return base_name, song_type_map[song_type], type_number
    return search_input, None, None

    
def main():
    song_typer = {1:'OP', 2:'ED', 3:'IN'}
    # Load the JSON file
    with open("songs.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Get search input from the user
    search_input = input("Enter search term: ")

    # Parse the input to extract filters
    search_term, song_type_filter, type_number_filter = parse_input(search_input)

    # Search for matching animes
    results = search_animes(data, search_term, song_type_filter, type_number_filter)

    # Display results
    if results:
        print("\nMatching Animes:")
        for i, (anime, matched_field) in enumerate(results, start=1):
            print(
                f"{i}. {anime[matched_field]} ({anime['songName']}) - "
                f"{song_typer[anime['songType']]} {anime['typeNumber']}"
            )
        
        # Allow the user to select a result to view its video720
        try:
            selection = int(input("\nSelect a number to view its video: "))
            if 1 <= selection <= len(results):
                selected_anime = results[selection - 1][0]
                print(f"https://naedist.animemusicquiz.com/{selected_anime['video720']}")
                webbrowser.open(f"https://naedist.animemusicquiz.com/{selected_anime['video720']}")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please input number.")
    else:
        print("No matching results found.")

if __name__ == "__main__":
    main()
