def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def unit_converter():
    conversion_dict = {
        "1": {"name": "Celsius to Fahrenheit", "function": celsius_to_fahrenheit, "unit_from": "Celsius", "unit_to": "Fahrenheit"},
        "2": {"name": "Fahrenheit to Celsius", "function": fahrenheit_to_celsius, "unit_from": "Fahrenheit", "unit_to": "Celsius"},
        "3": {"name": "Kilometers to Miles", "function": kilometers_to_miles, "unit_from": "Kilometers", "unit_to": "Miles"},
        "4": {"name": "Miles to Kilometers", "function": miles_to_kilometers, "unit_from": "Miles", "unit_to": "Kilometers"},
        "5": {"name": "Kilograms to Pounds", "function": kilograms_to_pounds, "unit_from": "Kilograms", "unit_to": "Pounds"},
        "6": {"name": "Pounds to Kilograms", "function": pounds_to_kilograms, "unit_from": "Pounds", "unit_to": "Kilograms"},
    }

    while True:
        print("\nSelect the conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Kilometers to Miles")
        print("4. Miles to Kilometers")
        print("5. Kilograms to Pounds")
        print("6. Pounds to Kilograms")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("Exiting converter...")
            break

        if choice in conversion_dict:
            try:
                value = float(input(f"Enter value in {conversion_dict[choice]['unit_from']}: "))
                result = conversion_dict[choice]["function"](value)
                print(f"{value} {conversion_dict[choice]['unit_from']} is {result} {conversion_dict[choice]['unit_to']}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        else:
            print("Invalid choice! Please select a valid option from the menu.")

if __name__ == "__main__":
    unit_converter()
