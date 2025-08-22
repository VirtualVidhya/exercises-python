# Event Planning Helper

from datetime import datetime

# Pre-initialize with sample events
events = {
    "2025/03/21": "Spring Fair",
    "2025/08/16": "Janmashtami Celebration", 
    "2025/12/25": "Winter Feast"
}

def display_menu():
    """Display the menu options"""
    print("\n### MENU: ###")
    print("1. Add event")
    print("2. Check event by date")
    print("3. List all events")
    print("4. Next event after date")
    print("5. Exit")

def format_date(year, month, day):
    """Format date as YYYY/MM/DD"""
    return f"{year:04d}/{month:02d}/{day:02d}"

def parse_date_input():
    """Parse user input for date in format YYYY MM DD"""
    try:
        date_input = input("Enter date (YYYY MM DD): ").strip().split()
        if len(date_input) != 3:
            raise ValueError("Invalid date format")
        
        year = int(date_input[0])
        month = int(date_input[1])
        day = int(date_input[2])
        
        # Validate date
        datetime(year, month, day)  # This will raise ValueError if invalid
        
        return format_date(year, month, day)
    except (ValueError, IndexError):
        print("Invalid date format. Please use YYYY MM DD format.")
        return None

def add_event():
    """Add a new event to the events dictionary"""
    date = parse_date_input()
    if date:
        event_description = input("Enter event description: ")
        events[date] = event_description
        print(f"Event added for {date}")

def check_event_by_date():
    """Check if there's an event on a specific date"""
    date = parse_date_input()
    if date:
        if date in events:
            print(f"Found! {date} - {events[date]}")
        else:
            print(f"No event on {date}")

def list_all_events():
    """List all events sorted chronologically"""
    print("All event dates:")
    if not events:
        print("No events scheduled.")
        return
    
    # Sort events by date
    sorted_dates = sorted(events.keys())
    for date in sorted_dates:
        print(f"{date} - {events[date]}")

def next_event_after_date():
    """Find the next event after a given date"""
    date = parse_date_input()
    if date:
        # Convert date strings to datetime objects for comparison
        target_date = datetime.strptime(date, "%Y/%m/%d")
        
        # Find events after the target date
        future_events = []
        for event_date in events:
            event_datetime = datetime.strptime(event_date, "%Y/%m/%d")
            if event_datetime > target_date:
                future_events.append((event_date, events[event_date]))
        
        if future_events:
            # Sort by date and get the earliest one
            future_events.sort(key=lambda x: x[0])
            next_date, next_event = future_events[0]
            print(f"Next event on {next_date} - {next_event}")
        else:
            print("No events scheduled after this date.")

def main():
    """Main program loop"""
    print("=== Event Planning Helper ===")
    print("Welcome to the school event management system!")
    
    while True:
        display_menu()
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            add_event()
        elif choice == "2":
            check_event_by_date()
        elif choice == "3":
            list_all_events()
        elif choice == "4":
            next_event_after_date()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()