#!/usr/bin/env python3
"""
Simple Addition Program

This program provides functionality to add numbers.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): First number (int or float)
        b (float): Second number (int or float)
    
    Returns:
        float: The sum of a and b
    """
    return a + b


def get_number(prompt: str) -> float:
    """
    Get a valid number from user input with error handling.
    
    Args:
        prompt (str): The prompt message to display to the user
        
    Returns:
        float: The number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            exit(0)


def add_multiple_numbers() -> None:
    """Add multiple numbers entered by the user."""
    print("\n--- Multiple Number Addition ---")
    numbers = []
    
    while True:
        try:
            count = int(input("How many numbers would you like to add? "))
            if count < 2:
                print("Please enter at least 2 numbers.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            return
    
    for i in range(count):
        number = get_number(f"Enter number {i + 1}: ")
        numbers.append(number)
    
    total = sum(numbers)
    numbers_str = " + ".join(str(num) for num in numbers)
    print(f"\nResult: {numbers_str} = {total}")


def main():
    """Main function for interactive addition program."""
    print("🔢 Interactive Addition Program")
    print("=" * 35)
    
    while True:
        print("\nChoose an option:")
        print("1. Add two numbers")
        print("2. Add multiple numbers")
        print("3. Exit")
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                print("\n--- Two Number Addition ---")
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                result = add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
                
            elif choice == "2":
                add_multiple_numbers()
                
            elif choice == "3":
                print("Thank you for using the Addition Program! 👋")
                break
                
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        
        # Ask if user wants to continue
        try:
            continue_choice = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("Thank you for using the Addition Program! 👋")
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break


if __name__ == "__main__":
    main()
