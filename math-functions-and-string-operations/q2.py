import math
import statistics
from fractions import Fraction


def get_co2_input():
    """Get CO₂ readings from user input."""
    while True:
        try:
            user_input = input("Enter CO₂ readings (ppm): ").strip()
            readings = [float(x) for x in user_input.split()]
            
            if len(readings) < 6:
                print("Please enter at least 6 CO₂ readings.")
                continue
            
            return readings
        except ValueError:
            print("Please enter valid numbers separated by spaces.")


def get_threshold_input():
    """Get threshold value from user input."""
    while True:
        try:
            threshold = float(input("Enter threshold (ppm): ").strip())
            return threshold
        except ValueError:
            print("Please enter a valid threshold value.")


def calculate_growth_factors(readings):
    """Calculate exact and decimal growth factors between consecutive readings."""
    exact_factors = []
    decimal_factors = []
    
    for i in range(len(readings) - 1):
        prev, curr = readings[i], readings[i + 1]
        
        # Calculate exact growth factor using Fraction
        exact_factor = Fraction(curr).limit_denominator() / Fraction(prev).limit_denominator()
        exact_factors.append(exact_factor)
        
        # Convert to decimal
        decimal_factor = float(exact_factor)
        decimal_factors.append(round(decimal_factor, 4))
    
    return exact_factors, decimal_factors


def calculate_log_rates(decimal_factors):
    """Calculate monthly growth rates using natural logarithm."""
    return [round(math.log(factor), 4) for factor in decimal_factors]


def calculate_range_stats(readings):
    """Calculate max, min, and range of readings."""
    max_reading = max(readings)
    min_reading = min(readings)
    range_ppm = max_reading - min_reading
    
    return max_reading, min_reading, range_ppm


def calculate_projection(last_reading, average_rate, months=12):
    """Calculate future projection using exponential growth model."""
    projection = last_reading * (1 + average_rate) ** months
    return round(projection, 2)


def calculate_months_to_threshold(threshold, last_reading, average_rate):
    """Calculate months needed to reach threshold and round up."""
    if average_rate <= 0:
        return float('inf')  # No growth, threshold never reached
    
    months = math.log(threshold / last_reading) / math.log(1 + average_rate)
    return math.ceil(months)


def display_results(readings, exact_factors, decimal_factors, log_rates, 
                   max_reading, min_reading, range_ppm, projection, months_to_threshold):
    """Display all results in the required format."""
    print("\nOriginal readings:")
    print(readings)
    
    print("\nExact growth factors:")
    print(exact_factors)
    
    print("\nDecimal growth factors:")
    print(decimal_factors)
    
    print("\nMonthly log-rates:")
    print(log_rates)
    
    print(f"\nMax reading: {int(max_reading)}")
    print(f"Min reading: {int(min_reading)}")
    print(f"Range: {int(range_ppm)}")
    
    print(f"\nProjected CO₂ after 12 months: {projection} ppm")
    
    print(f"\nMonths to reach threshold: {months_to_threshold}")


def main():
    """Main function to orchestrate the CO₂ analysis."""
    # Get input
    readings = get_co2_input()
    threshold = get_threshold_input()
    
    # Calculate growth factors
    exact_factors, decimal_factors = calculate_growth_factors(readings)
    
    # Calculate logarithmic rates
    log_rates = calculate_log_rates(decimal_factors)
    
    # Calculate range statistics
    max_reading, min_reading, range_ppm = calculate_range_stats(readings)
    
    # Calculate average rate for projections
    average_rate = statistics.mean(log_rates)
    
    # Calculate future projection
    last_reading = readings[-1]
    projection = calculate_projection(last_reading, average_rate)
    
    # Calculate months to threshold
    months_to_threshold = calculate_months_to_threshold(threshold, last_reading, average_rate)
    
    # Display results
    display_results(readings, exact_factors, decimal_factors, log_rates,
                   max_reading, min_reading, range_ppm, projection, months_to_threshold)


if __name__ == "__main__":
    main()