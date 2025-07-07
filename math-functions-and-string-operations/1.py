import statistics
import math


def get_magnitude_input():
    """Get magnitude readings from user input."""
    while True:
        try:
            user_input = input("Enter magnitudes: ").strip()
            magnitudes = [float(x) for x in user_input.split()]
            
            if len(magnitudes) < 10:
                print("Please enter at least 10 magnitude values.")
                continue
            
            return magnitudes
        except ValueError:
            print("Please enter valid numbers separated by spaces.")


def calculate_amplitude_ratios(magnitudes):
    """Calculate amplitude ratios between consecutive magnitude pairs."""
    ratios = []
    for i in range(len(magnitudes) - 1):
        m1, m2 = magnitudes[i], magnitudes[i + 1]
        # amplitude_ratio = 10^(m2 - m1)
        ratio = 10 ** (m2 - m1)
        ratios.append(round(ratio, 2))
    return ratios


def calculate_statistics(magnitudes):
    """Calculate mean, variance, and mode of magnitudes."""
    mean = statistics.mean(magnitudes)
    variance = statistics.variance(magnitudes)
    mode = statistics.mode(magnitudes)
    
    return round(mean, 1), round(variance, 2), mode


def get_unique_count(magnitudes):
    """Get count of unique magnitudes using set."""
    return len(set(magnitudes))


def create_chart_bins(magnitudes):
    """Create chart bins by flooring each magnitude."""
    return [math.floor(mag) for mag in magnitudes]


def display_results(magnitudes, ratios, mean, variance, mode, unique_count, chart_bins):
    """Display all results in the required format."""
    print("\nOriginal magnitudes:")
    print(magnitudes)
    
    print("\nAmplitude ratios between each pair:")
    print(ratios)
    
    print("\nMagnitude stats:")
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Mode: {mode}")
    
    print(f"\nNumber of distinct magnitudes: {unique_count}")
    
    print("\nChart bins (floored values):")
    print(chart_bins)


def main():
    """Main function to orchestrate the earthquake analysis."""
    # Get input
    magnitudes = get_magnitude_input()
    
    # Calculate amplitude ratios
    amplitude_ratios = calculate_amplitude_ratios(magnitudes)
    
    # Calculate statistics
    mean, variance, mode = calculate_statistics(magnitudes)
    
    # Get unique count
    unique_count = get_unique_count(magnitudes)
    
    # Create chart bins
    chart_bins = create_chart_bins(magnitudes)
    
    # Display results
    display_results(magnitudes, amplitude_ratios, mean, variance, mode, unique_count, chart_bins)


if __name__ == "__main__":
    main()