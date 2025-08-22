def initialize_data():
    """Initialize the market data with some sample entries."""
    return {
        'vendors': {
            'Green Valley Farm': {'products': {'Tomatoes': 45, 'Lettuce': 32}, 'ratings': [4.5, 4.8, 4.2]},
            'Sunny Acres': {'products': {'Apples': 38, 'Honey': 12}, 'ratings': [4.1, 3.9, 4.3]},
            'Mountain View Dairy': {'products': {'Cheese': 25, 'Milk': 18}, 'ratings': [4.7, 4.9, 4.6]}
        }
    }

def calculate_vendor_totals(market_data):
    """Calculate total units sold per vendor."""
    vendor_totals = {}
    for vendor, data in market_data['vendors'].items():
        total_units = sum(data['products'].values())
        vendor_totals[vendor] = total_units
    return vendor_totals

def calculate_product_aggregates(market_data):
    """Calculate aggregate sales per product and identify top seller."""
    product_totals = {}
    for vendor_data in market_data['vendors'].values():
        for product, quantity in vendor_data['products'].items():
            product_totals[product] = product_totals.get(product, 0) + quantity
    
    top_product = max(product_totals.items(), key=lambda x: x[1]) if product_totals else ("None", 0)
    return product_totals, top_product

def calculate_vendor_ratings(market_data):
    """Calculate average ratings per vendor and identify highly rated vendors."""
    vendor_ratings = {}
    highly_rated_vendors = []
    
    for vendor, data in market_data['vendors'].items():
        if data['ratings']:
            avg_rating = sum(data['ratings']) / len(data['ratings'])
            vendor_ratings[vendor] = avg_rating
            if avg_rating >= 4.0:
                highly_rated_vendors.append((vendor, avg_rating))
        else:
            vendor_ratings[vendor] = 0.0
    
    return vendor_ratings, highly_rated_vendors

def display_comprehensive_summary(market_data):
    """Display comprehensive sales and rating summaries."""
    print("\n" + "="*60)
    print("COMPREHENSIVE MARKET PERFORMANCE SUMMARY")
    print("="*60)
    
    # Vendor totals
    vendor_totals = calculate_vendor_totals(market_data)
    print("\nTOTAL UNITS SOLD PER VENDOR:")
    print("-" * 40)
    for vendor, total in sorted(vendor_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {vendor:<25} {total:>6} units")
    
    # Product aggregates
    product_totals, top_product = calculate_product_aggregates(market_data)
    print(f"\nTOP-SELLING PRODUCT:")
    print("-" * 40)
    print(f"  {top_product[0]} - {top_product[1]} units sold")
    
    print(f"\nALL PRODUCT SALES:")
    print("-" * 40)
    for product, total in sorted(product_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {product:<20} {total:>6} units")
    
    # Vendor ratings
    vendor_ratings, highly_rated_vendors = calculate_vendor_ratings(market_data)
    print(f"\nVENDOR RATINGS:")
    print("-" * 40)
    for vendor, rating in sorted(vendor_ratings.items(), key=lambda x: x[1], reverse=True):
        print(f"  {vendor:<25} {rating:>6.2f}/5.0")
    
    print(f"\nHIGHLY RATED VENDORS (4.0+):")
    print("-" * 40)
    if highly_rated_vendors:
        for vendor, rating in sorted(highly_rated_vendors, key=lambda x: x[1], reverse=True):
            print(f"  {vendor:<25} {rating:>6.2f}/5.0")
    else:
        print("  No vendors currently rated 4.0 or higher")

def add_live_update(market_data):
    """Add a live update with vendor, product, quantity, and rating."""
    print("\n" + "="*50)
    print("ADD LIVE MARKET UPDATE")
    print("="*50)
    
    # Get vendor name
    vendor_name = input("Enter vendor name: ").strip()
    if not vendor_name:
        print("Error: Vendor name cannot be empty.")
        return False
    
    # Get product name
    product_name = input("Enter product name: ").strip()
    if not product_name:
        print("Error: Product name cannot be empty.")
        return False
    
    # Get quantity
    try:
        quantity = int(input("Enter quantity sold: "))
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return False
    except ValueError:
        print("Error: Please enter a valid number for quantity.")
        return False
    
    # Get rating
    try:
        rating = float(input("Enter customer rating (1.0-5.0): "))
        if not (1.0 <= rating <= 5.0):
            print("Error: Rating must be between 1.0 and 5.0.")
            return False
    except ValueError:
        print("Error: Please enter a valid number for rating.")
        return False
    
    # Add or update vendor data
    if vendor_name not in market_data['vendors']:
        market_data['vendors'][vendor_name] = {'products': {}, 'ratings': []}
    
    # Update product quantity
    current_qty = market_data['vendors'][vendor_name]['products'].get(product_name, 0)
    market_data['vendors'][vendor_name]['products'][product_name] = current_qty + quantity
    
    # Add rating
    market_data['vendors'][vendor_name]['ratings'].append(rating)
    
    print(f"Successfully added: {quantity} units of {product_name} from {vendor_name} (Rating: {rating}/5.0)")
    return True

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("FARMERS' CO-OP MARKET PERFORMANCE TRACKER")
    print("="*50)
    print("1. View comprehensive sales and rating summaries")
    print("2. Enter a live update (vendor, product, quantity, rating)")
    print("3. Exit program")
    print("-" * 50)

def get_user_choice():
    """Get and validate user menu choice."""
    while True:
        try:
            choice = input("Enter your choice (1-3): ").strip()
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print("Please enter 1, 2, or 3.")
        except (ValueError, KeyboardInterrupt):
            print("Invalid input. Please enter 1, 2, or 3.")

def main():
    """Main program loop."""
    print("Welcome to the Farmers' Co-op Market Performance Tracker!")
    
    # Initialize market data
    market_data = initialize_data()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            display_comprehensive_summary(market_data)
            
        elif choice == 2:
            if add_live_update(market_data):
                print("\nUpdated Market Summary:")
                print("=" * 30)
                
                # Display updated calculations
                vendor_totals = calculate_vendor_totals(market_data)
                product_totals, top_product = calculate_product_aggregates(market_data)
                vendor_ratings, highly_rated_vendors = calculate_vendor_ratings(market_data)
                
                print(f"\nTotal units by vendor:")
                for vendor, total in sorted(vendor_totals.items(), key=lambda x: x[1], reverse=True):
                    print(f"  {vendor}: {total} units")
                
                print(f"\nTop-selling product: {top_product[0]} ({top_product[1]} units)")
                
                print(f"\nVendors rated 4.0+:")
                if highly_rated_vendors:
                    for vendor, rating in sorted(highly_rated_vendors, key=lambda x: x[1], reverse=True):
                        print(f"  {vendor}: {rating:.2f}/5.0")
                else:
                    print("  None currently")
            
        elif choice == 3:
            print("\nThank you for using the Market Performance Tracker!")
            print("Have a great market day!")
            break
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please restart the program.")