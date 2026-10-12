"""
Simple Calculator - Interactive Command-Line Application.

This module provides fundamental arithmetic operations through an interactive
console interface. It supports addition, subtraction, multiplication, division,
modulus, and exponentiation with input validation and error handling.
"""

import math
import sys


def add(first_number: float, second_number: float) -> float:
    """Return the sum of two floating-point numbers."""
    result = first_number + second_number
    if not math.isfinite(result):
        raise ValueError("Calculation resulted in a non-finite number.")
    return result


def subtract(first_number: float, second_number: float) -> float:
    """Return the difference between two floating-point numbers."""
    result = first_number - second_number
    if not math.isfinite(result):
        raise ValueError("Calculation resulted in a non-finite number.")
    return result


def multiply(first_number: float, second_number: float) -> float:
    """Return the product of two floating-point numbers."""
    result = first_number * second_number
    if not math.isfinite(result):
        raise ValueError("Calculation resulted in a non-finite number.")
    return result


def divide(first_number: float, second_number: float) -> float:
    """
    Return the quotient of two floating-point numbers.

    Raises:
        ZeroDivisionError: If the second number (denominator) is zero.
        ValueError: If the result is not finite.
    """
    if second_number == 0.0:
        raise ZeroDivisionError("Division by zero is undefined.")
    result = first_number / second_number
    if not math.isfinite(result):
        raise ValueError("Calculation resulted in a non-finite number.")
    return result


def modulus(first_number: float, second_number: float) -> float:
    """
    Return the remainder of two floating-point numbers.

    Raises:
        ZeroDivisionError: If the second number (divisor) is zero.
        ValueError: If the result is not finite.
    """
    if second_number == 0.0:
        raise ZeroDivisionError("Modulo by zero is undefined.")
    result = first_number % second_number
    if not math.isfinite(result):
        raise ValueError("Calculation resulted in a non-finite number.")
    return result


def power(first_number: float, second_number: float) -> float:
    """
    Return the first number raised to the power of the second number.

    Raises:
        ZeroDivisionError: If zero is raised to a negative exponent.
        ValueError: If calculation results in a complex or non-finite number.
        OverflowError: If calculation overflows float representation.
    """
    if first_number == 0.0 and second_number < 0.0:
        raise ZeroDivisionError("Zero cannot be raised to a negative power.")

    # In Python, negative base with fractional exponent produces a complex number
    if first_number < 0.0 and not second_number.is_integer():
        raise ValueError("Result is a complex number; real numbers only.")

    try:
        result = first_number ** second_number
    except OverflowError:
        raise OverflowError("Arithmetic overflow occurred in exponentiation.")

    # Check for complex result if native ** returned complex type
    if isinstance(result, complex):
        raise ValueError("Result is a complex number; real numbers only.")

    if not math.isfinite(result):
        raise ValueError("Calculation resulted in a non-finite number.")

    return float(result)


def display_menu() -> None:
    """Display the main calculator menu."""
    print()
    print("=== PYTHON CLI CALCULATOR ===")
    print()
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (x^y)")
    print("7. Exit Application")
    print()


def get_number(prompt: str) -> float:
    """
    Prompt the user for a numeric input and convert it to float.

    Repeats prompting until a valid number is provided. Catches ValueError
    for non-numeric or empty input.
    """
    while True:
        raw_input = input(prompt).strip()
        try:
            return float(raw_input)
        except ValueError:
            print("[ERROR] Invalid input! Please enter a valid number.")


def perform_calculation(choice: str) -> None:
    """
    Coordinate number inputs, arithmetic calculation, and result formatting.

    Args:
        choice: Selected menu option ('1' to '6').
    """
    # Define operation labels and symbols
    operations = {
        "1": {"prompt1": "Enter First Number: ", "prompt2": "Enter Second Number: ", "symbol": "+"},
        "2": {"prompt1": "Enter First Number: ", "prompt2": "Enter Second Number: ", "symbol": "-"},
        "3": {"prompt1": "Enter First Number: ", "prompt2": "Enter Second Number: ", "symbol": "*"},
        "4": {"prompt1": "Enter Numerator: ", "prompt2": "Enter Denominator: ", "symbol": "/"},
        "5": {"prompt1": "Enter First Number: ", "prompt2": "Enter Second Number: ", "symbol": "%"},
        "6": {"prompt1": "Enter Base: ", "prompt2": "Enter Exponent: ", "symbol": "^"},
    }

    config = operations[choice]
    num1 = get_number(config["prompt1"])
    num2 = get_number(config["prompt2"])

    # Division by zero pre-check and error handling
    if choice == "4" and num2 == 0.0:
        print()
        print("[ERROR] Division by zero is undefined! Please enter a non-zero denominator.")
        return

    # Modulus by zero pre-check and error handling
    if choice == "5" and num2 == 0.0:
        print()
        print("[ERROR] Modulo by zero is undefined! Please enter a non-zero second operand.")
        return

    try:
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = modulus(num1, num2)
        elif choice == "6":
            result = power(num1, num2)
        else:
            print("[ERROR] Unrecognized operation selection.")
            return

        print()
        print(f"-> Result: {num1:.2f} {config['symbol']} {num2:.2f} = {result:.2f}")

    except ZeroDivisionError as err:
        print()
        print(f"[ERROR] {err}")
    except OverflowError:
        print()
        print("[ERROR] Calculation overflow! Result is too large to represent.")
    except ValueError as err:
        print()
        print(f"[ERROR] {err}")


def main() -> None:
    """Run the main loop for the CLI calculator application."""
    while True:
        try:
            display_menu()
            choice = input("Select Operation (1-7): ").strip()

            if choice == "7":
                print()
                print("Thank you for using the Python CLI Calculator. Goodbye!")
                break
            elif choice in {"1", "2", "3", "4", "5", "6"}:
                perform_calculation(choice)
            else:
                print()
                print("[ERROR] Invalid selection! Please enter a choice between 1 and 7.")

        except (KeyboardInterrupt, EOFError):
            print()
            print("Session interrupted. Thank you for using the Python CLI Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
