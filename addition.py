#!/usr/bin/env python3
"""
Simple Addition Program

This program provides functionality to add numbers.
"""


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def main():
    """Main function to demonstrate addition."""
    print("Addition Program")
    print("-" * 20)
    
    # Example 1: Adding two integers
    num1 = 5
    num2 = 3
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
    
    # Example 2: Adding two floats
    num3 = 10.5
    num4 = 4.5
    result2 = add(num3, num4)
    print(f"{num3} + {num4} = {result2}")
    
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
