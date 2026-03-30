# Name: Shannon Blake
# Date: March 30, 2026
# CSD325-T301 M2.2
# Purpose: Convert a temperature value between Celsius and Fahrenheit.


def get_user_input():
    # Ask the user for a temperature value and unit
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip()
    return value, unit
 
 
def convert_temperature(value, unit):
    # Convert Celsius to Fahrenheit
    if unit.upper() == 'C':
        converted = (value * 9 / 5) + 32
        converted_unit = 'F'
 
    # Convert Fahrenheit to Celsius
    elif unit.upper() == 'F':
        converted = (value - 32) * 5 / 9
        converted_unit = 'C'
 
    # Raise an error if the unit is not recognized
    else:
        raise ValueError(f"Unknown unit '{unit}'. Please use 'C' or 'F'.")
 
    return converted, converted_unit
 
 
def display_result(original_value, original_unit, converted_value, converted_unit):
    # Print the conversion result to the user
    print(f"\n{original_value}° {original_unit} = {converted_value:.2f}° {converted_unit}")
 
 
def main():
    print("=== Temperature Converter ===")
 
    # Keep asking until the user enters valid input
    while True:
        try:
            # Get temperature value and unit from the user
            value, unit = get_user_input()
 
            # Check that the unit is C or F — re-prompt if not
            if unit.upper() not in ('C', 'F'):
                print("Invalid unit. Please enter C or F.\n")
 
            # Valid input — exit the loop
            else:
                break
 
        # Catch non-numeric temperature values and re-prompt
        except ValueError:
            print("Invalid temperature value. Please enter a number.\n")
 
    # Pass the valid input to the conversion function
    converted, converted_unit = convert_temperature(value, unit)
 
    # Display the result
    display_result(value, unit, converted, converted_unit)
 
 
# Run the program
if __name__ == "__main__":
    main()
