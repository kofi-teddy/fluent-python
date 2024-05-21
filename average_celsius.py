from typing import List


def average_celsius(fahrenheit_readings: List[float]) -> float:
    """
    Calculates the average Celsius temperature from a list of Fahrenheit readings.

    Args:
        fahrenheit_readings: A list of Fahrenheit temperature readings.

    Returns:
        The mean average Celsius temperature.

    """
    # Collect Celsius numbers here:
    celsius_numbers = []
    
    # Convert each reading to Celsius and add to array:
    for fahrenheit_reading in fahrenheit_readings:
        celsius_conversion = (fahrenheit_reading - 32) / 1.8
        celsius_numbers.append(celsius_conversion)
    
    # Get sum of all Celsius numbers:
    total = sum(celsius_numbers)
    
    # Return mean average:
    return total / len(celsius_numbers)


# Example usage:
readings = [32, 68, 77, 104]
average_temp = average_celsius(readings)
print(f"The average Celsius temperature is: {average_temp}")
