import math


def get_rise_input():
    """Get rise measurements from user input."""
    while True:
        try:
            user_input = input("Enter rises (m): ").strip()
            rises = [float(x) for x in user_input.split()]
            return rises
        except ValueError:
            print("Please enter valid numbers separated by spaces.")


def get_run_input():
    """Get run measurements from user input."""
    while True:
        try:
            user_input = input("Enter runs (m): ").strip()
            runs = [float(x) for x in user_input.split()]
            return runs
        except ValueError:
            print("Please enter valid numbers separated by spaces.")


def get_max_safe_angle():
    """Get maximum safe angle from user input."""
    while True:
        try:
            angle = float(input("Enter maximum safe angle (°): ").strip())
            return angle
        except ValueError:
            print("Please enter a valid angle value.")


def validate_input_lengths(rises, runs):
    """Validate that rise and run lists have the same length."""
    if len(rises) != len(runs):
        raise ValueError("Rise and run lists must have the same length.")


def calculate_slope_angles(rises, runs):
    """Calculate slope angles in both radians and degrees."""
    angles_rad = []
    angles_deg = []
    
    for rise, run in zip(rises, runs):
        if run == 0:
            raise ValueError("Run cannot be zero (vertical slope undefined).")
        
        angle_rad = math.atan(rise / run)
        angle_deg = math.degrees(angle_rad)
        
        angles_rad.append(angle_rad)
        angles_deg.append(round(angle_deg, 2))
    
    return angles_rad, angles_deg


def calculate_gravity_components(angles_rad):
    """Calculate vertical and horizontal gravity components."""
    vertical_ratios = []
    horizontal_ratios = []
    
    for angle_rad in angles_rad:
        vertical_ratio = math.sin(angle_rad)
        horizontal_ratio = math.cos(angle_rad)
        
        vertical_ratios.append(round(vertical_ratio, 2))
        horizontal_ratios.append(round(horizontal_ratio, 2))
    
    return vertical_ratios, horizontal_ratios


def filter_unsafe_segments(rises, runs, angles_deg, max_safe_angle):
    """Filter segments that exceed the maximum safe angle."""
    segments_data = list(zip(range(len(rises)), rises, runs, angles_deg))
    
    # Use filter() to select unsafe segments
    unsafe_segments = list(filter(lambda seg: seg[3] > max_safe_angle, segments_data))
    
    return unsafe_segments


def display_segment_data(rises, runs, angles_deg, vertical_ratios, horizontal_ratios):
    """Display data for all segments."""
    print("\nSegment data:")
    for i, (rise, run, angle, v_ratio, h_ratio) in enumerate(
        zip(rises, runs, angles_deg, vertical_ratios, horizontal_ratios), 1
    ):
        print(f"{i}. Rise: {int(rise):2}, Run: {int(run):2} - Angle: {angle:5.2f}° | "
              f"Vertical ratio: {v_ratio:.2f}, Horizontal ratio: {h_ratio:.2f}")


def display_unsafe_segments(unsafe_segments, max_safe_angle):
    """Display unsafe segments that exceed the maximum safe angle."""
    print(f"\nUnsafe segments (angle > {max_safe_angle}°):")
    
    if not unsafe_segments:
        print("No unsafe segments found.")
        return
    
    for index, rise, run, angle in unsafe_segments:
        print(f"{index + 1}. Rise: {int(rise):2}, Run: {int(run):2} → Angle: {angle:.2f}°")


def main():
    """Main function to orchestrate the road slope analysis."""
    try:
        # Get input
        rises = get_rise_input()
        runs = get_run_input()
        max_safe_angle = get_max_safe_angle()
        
        # Validate input
        validate_input_lengths(rises, runs)
        
        # Calculate slope angles
        angles_rad, angles_deg = calculate_slope_angles(rises, runs)
        
        # Calculate gravity components
        vertical_ratios, horizontal_ratios = calculate_gravity_components(angles_rad)
        
        # Filter unsafe segments
        unsafe_segments = filter_unsafe_segments(rises, runs, angles_deg, max_safe_angle)
        
        # Display results
        display_segment_data(rises, runs, angles_deg, vertical_ratios, horizontal_ratios)
        display_unsafe_segments(unsafe_segments, max_safe_angle)
        
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero encountered.")


if __name__ == "__main__":
    main()