import json
import webbrowser
import re

def search_animes(data, input_value):
    """
    Searches the JSON data for partial matches across specified fields.
    
    Parameters:
        data (list): List of anime data.
        input_value (str): The input value to match.
    
    Returns:
        list: List of tuples with matching anime and the field it matched on.
    """
    fields_to_search = ["animeEnglishName", "animeRomajiName", "songArtist", "songName"]
    results = []

    for anime in data:
        for field in fields_to_search:
            anime_field_clean = re.sub('[^a-zA-Z\d\s]+', ' ', anime.get(field, ""))
            if input_value.lower() in anime_field_clean.lower():
                results.append((anime, field))
                break  # Stop checking other fields once a match is found for this anime

    return results

def song_typer(songtype):
    # print(type(songtype))
    if songtype == 1 :
        return "OP"
    elif songtype == 2 :
        return "ED"
    else : # 3
        return "IN"

def main():
    # Load the JSON file
    with open("songs.json", "r", encoding="utf-8") as file:             ### edit this line to insert custom name!
        data = json.load(file)

    # Get search input from the user
    # search_input = input("Enter search term: ").strip()      #.strip gets rid of whitespaces
    search_input = input("Enter search term: ")

    # Search for matching animes
    results = search_animes(data, search_input)

    # Display results
    if results:
        print("\nMatching Animes:")
        for i, (anime, matched_field) in enumerate(results, start=1):
            print(
                f"{i}. {anime[matched_field]} ({anime['songName']}) - "
                f"{song_typer(anime['songType'])} {anime['typeNumber']}"
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
