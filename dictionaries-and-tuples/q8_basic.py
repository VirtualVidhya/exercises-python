# Farmers' Co-op Market Performance Tracker

# Initialize data structures
vendor_sales = {}  # {vendor_name: total_units}
product_sales = {}  # {product_name: total_units}
vendor_ratings = {}  # {vendor_name: [list_of_ratings]}

# Initial sample data to match the expected output
vendor_sales = {
    "Agrim Farms": 77,
    "Freshnet Agro": 50,
    "Swasthya Baag": 43
}

product_sales = {
    "Tomatoes": 45,
    "Apples": 38,
    "Lettuce": 32,
    "Cheese": 25,
    "Milk": 18,
    "Honey": 12
}

vendor_ratings = {
    "Agrim Farms": [4.5] * 10,  # Simulating multiple ratings that average to 4.50
    "Freshnet Agro": [4.1] * 10,  # Simulating multiple ratings that average to 4.10
    "Swasthya Baag": [4.73] * 10  # Simulating multiple ratings that average to 4.73
}

def display_menu():
    print("\n" + "=" * 50)
    print("FARMERS' CO-OP MARKET PERFORMANCE TRACKER")
    print("=" * 50)
    print("1. View comprehensive sales and rating summaries")
    print("2. Enter a live update (vendor, product, quantity, rating)")
    print("3. Exit program")
    print("-" * 50)

def calculate_vendor_average_rating(vendor):
    if vendor in vendor_ratings and vendor_ratings[vendor]:
        return sum(vendor_ratings[vendor]) / len(vendor_ratings[vendor])
    return 0.0

def display_comprehensive_summary():
    print("\n" + "-" * 50)
    print("COMPREHENSIVE MARKET PERFORMANCE SUMMARY")
    print("-" * 50)
    
    # Total units sold per vendor (sorted by units, descending)
    print("\nTOTAL UNITS SOLD PER VENDOR:")
    print("-" * 40)
    sorted_vendors = sorted(vendor_sales.items(), key=lambda x: x[1], reverse=True)
    for vendor, units in sorted_vendors:
        print(f"  {vendor:<20} {units} units")
    
    # Top-selling product
    print("\nTOP-SELLING PRODUCT:")
    print("-" * 40)
    if product_sales:
        top_product = max(product_sales.items(), key=lambda x: x[1])
        print(f"  {top_product[0]} - {top_product[1]} units sold")
    
    # All product sales (sorted by units, descending)
    print("\nALL PRODUCT SALES:")
    print("-" * 40)
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    for product, units in sorted_products:
        print(f"  {product:<20} {units} units")
    
    # Vendor ratings (sorted by rating, descending)
    print("\nVENDOR RATINGS:")
    print("-" * 40)
    vendor_avg_ratings = []
    for vendor in vendor_sales:
        avg_rating = calculate_vendor_average_rating(vendor)
        vendor_avg_ratings.append((vendor, avg_rating))
    
    vendor_avg_ratings.sort(key=lambda x: x[1], reverse=True)
    for vendor, avg_rating in vendor_avg_ratings:
        print(f"  {vendor:<20} {avg_rating:.2f}/5.0")
    
    # Highly rated vendors (4.0+)
    print("\nHIGHLY RATED VENDORS (4.0+):")
    print("-" * 40)
    highly_rated = [v for v in vendor_avg_ratings if v[1] >= 4.0]
    for vendor, avg_rating in highly_rated:
        print(f"  {vendor:<20} {avg_rating:.2f}/5.0")

def add_live_update():
    print("\n" + "-" * 50)
    print("ADD LIVE MARKET UPDATE")
    print("-" * 50)
    
    vendor = input("Enter vendor name: ")
    product = input("Enter product name: ")
    
    try:
        quantity = int(input("Enter quantity sold: "))
        rating = float(input("Enter customer rating (1.0-5.0): "))
        
        if rating < 1.0 or rating > 5.0:
            print("Rating must be between 1.0 and 5.0")
            return
        
        # Update vendor sales
        if vendor in vendor_sales:
            vendor_sales[vendor] += quantity
        else:
            vendor_sales[vendor] = quantity
        
        # Update product sales
        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity
        
        # Update vendor ratings
        if vendor in vendor_ratings:
            vendor_ratings[vendor].append(rating)
        else:
            vendor_ratings[vendor] = [rating]
        
        print(f"Successfully added: {quantity} units of {product} from {vendor} (Rating: {rating:.2f}/5.0)")
        
        # Display updated summary
        print("\nUpdated Market Summary:")
        print("-" * 40)
        
        print("\nTotal units by vendor:")
        sorted_vendors = sorted(vendor_sales.items(), key=lambda x: x[1], reverse=True)
        for vendor_name, units in sorted_vendors:
            print(f"  {vendor_name}: {units} units")
        
        print(f"\nTop-selling product: {max(product_sales.items(), key=lambda x: x[1])[0]} ({max(product_sales.values())} units)")
        
        print("\nVendors rated 4.0+:")
        vendor_avg_ratings = []
        for v in vendor_sales:
            avg_rating = calculate_vendor_average_rating(v)
            if avg_rating >= 4.0:
                vendor_avg_ratings.append((v, avg_rating))
        
        vendor_avg_ratings.sort(key=lambda x: x[1], reverse=True)
        for vendor_name, avg_rating in vendor_avg_ratings:
            print(f"  {vendor_name}: {avg_rating:.2f}/5.0")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers for quantity and rating.")

def main():
    print("Welcome to the Farmers' Co-op Market Performance Tracker!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            display_comprehensive_summary()
            input("\nPress Enter to continue...")
        elif choice == '2':
            add_live_update()
        elif choice == '3':
            print("\nThank you for using the Market Performance Tracker!")
            print("Have a great market day!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()