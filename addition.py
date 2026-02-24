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


def main():
    """Main function to demonstrate addition."""
    print("Addition Program")
    print("-" * 20)
    
    # Example 1: Adding two integers
    first_integer = 5
    second_integer = 3
    result = add(first_integer, second_integer)
    print(f"{first_integer} + {second_integer} = {result}")
    
    # Example 2: Adding two floats
    first_float = 10.5
    second_float = 4.5
    result2 = add(first_float, second_float)
    print(f"{first_float} + {second_float} = {result2}")
    
    # Example 3: Interactive addition
    print("\nTry it yourself:")
    try:
        user_num1 = float(input("Enter first number: "))
        user_num2 = float(input("Enter second number: "))
        user_result = add(user_num1, user_num2)
        print(f"{user_num1} + {user_num2} = {user_result}")
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")


if __name__ == "__main__":
    main()
