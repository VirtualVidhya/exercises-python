# World Treasure Map Assistant

# Dictionary of famous treasures/places with their GPS coordinates
treasure_map = {
    "Taj Mahal": {"latitude": 27.1751, "longitude": 78.0421},
    "Statue of Liberty": {"latitude": 40.6892, "longitude": -74.0445},
    "Eiffel Tower": {"latitude": 48.8584, "longitude": 2.2945},
    "Great Wall of China": {"latitude": 40.4319, "longitude": 116.5704},
    "Machu Picchu": {"latitude": -13.1631, "longitude": -72.5450},
    "Pyramid of Giza": {"latitude": 29.9792, "longitude": 31.1342},
    "Colosseum": {"latitude": 41.8902, "longitude": 12.4922},
    "Christ the Redeemer": {"latitude": -22.9519, "longitude": -43.2105},
    "Petra": {"latitude": 30.3285, "longitude": 35.4444},
    "Angkor Wat": {"latitude": 13.4125, "longitude": 103.8670},
    "Stonehenge": {"latitude": 51.1789, "longitude": -1.8262},
    "Mount Rushmore": {"latitude": 43.8791, "longitude": -103.4591},
    "Sydney Opera House": {"latitude": -33.8568, "longitude": 151.2153},
    "Big Ben": {"latitude": 51.5007, "longitude": -0.1246},
    "Golden Gate Bridge": {"latitude": 37.8199, "longitude": -122.4783}
}

def search_treasure(place_name):
    """Search for a place in the treasure map database"""
    # Check if the place exists in our database
    if place_name in treasure_map:
        lat = treasure_map[place_name]["latitude"]
        lng = treasure_map[place_name]["longitude"]
        print(f"Found! {place_name} at latitude {lat} and longitude {lng}")
    else:
        print(f"Not Found! Sorry, {place_name} is not in our database.")

def main():
    """Main program loop"""
    print("=== World Treasure Map Assistant ===")
    print("Enter the name of a famous treasure/place to get GPS coordinates!")
    print("Available places include: Taj Mahal, Statue of Liberty, Eiffel Tower, etc.")
    print("Type 'quit' to exit.\n")
    
    while True:
        place_name = input("Enter place name: ").strip()
        
        if place_name.lower() == 'quit':
            print("Thank you for using the World Treasure Map Assistant!")
            break
        
        if place_name:
            search_treasure(place_name)
        else:
            print("Please enter a valid place name.")
        
        print()  # Add blank line for readability

if __name__ == "__main__":
    main()