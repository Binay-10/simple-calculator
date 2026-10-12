"""
Unit tests for the Simple Calculator project.

Tests all arithmetic functions, division-by-zero checks, input validation,
error handling, and continuous CLI execution flow.
"""

import io
import math
import sys
import unittest
from unittest.mock import patch

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    get_number,
    perform_calculation,
    main,
)


class TestArithmeticOperations(unittest.TestCase):
    """Test individual mathematical operations for accuracy and edge cases."""

    def test_addition_standard(self):
        """TEST 1: Addition of positive floating-point numbers."""
        result = add(18.5, 6.5)
        self.assertAlmostEqual(result, 25.0, places=2)

    def test_subtraction_standard(self):
        """TEST 2: Subtraction preserving operand order."""
        result = subtract(18.5, 6.5)
        self.assertAlmostEqual(result, 12.0, places=2)

    def test_multiplication_standard(self):
        """TEST 3: Multiplication of floating-point numbers."""
        result = multiply(18.5, 6.5)
        self.assertAlmostEqual(result, 120.25, places=2)

    def test_division_standard(self):
        """TEST 4: Division with non-zero denominator."""
        result = divide(45.0, 5.0)
        self.assertAlmostEqual(result, 9.0, places=2)

    def test_division_by_zero(self):
        """TEST 5: Division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(45.0, 0.0)
        with self.assertRaises(ZeroDivisionError):
            divide(45.0, -0.0)

    def test_modulus_standard(self):
        """TEST 6: Modulus calculation."""
        result = modulus(10.0, 3.0)
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_modulus_by_zero(self):
        """TEST 7: Modulus by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            modulus(10.0, 0.0)
        with self.assertRaises(ZeroDivisionError):
            modulus(10.0, -0.0)

    def test_exponentiation_standard(self):
        """TEST 8: Exponentiation calculation."""
        result = power(2.0, 3.0)
        self.assertAlmostEqual(result, 8.0, places=2)

    def test_decimal_precision(self):
        """TEST 14: Decimal precision with fractional values."""
        result = add(0.1, 0.2)
        self.assertEqual(f"{result:.2f}", "0.30")

    def test_negative_numbers(self):
        """TEST 15: Arithmetic behavior with negative operands."""
        self.assertAlmostEqual(add(-5.0, -3.0), -8.0, places=2)
        self.assertAlmostEqual(subtract(-5.0, -3.0), -2.0, places=2)
        self.assertAlmostEqual(multiply(-4.0, 2.5), -10.0, places=2)
        self.assertAlmostEqual(divide(-9.0, 3.0), -3.0, places=2)
        self.assertAlmostEqual(power(-2.0, 3.0), -8.0, places=2)
        self.assertAlmostEqual(power(2.0, -2.0), 0.25, places=2)

    def test_non_finite_and_overflow(self):
        """TEST 16: Handling overflow and non-finite / complex results."""
        # Zero raised to negative power raises ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            power(0.0, -1.0)

        # Negative base with fractional exponent raises ValueError (complex)
        with self.assertRaises(ValueError):
            power(-4.0, 0.5)

        # Extremely large exponentiation raises OverflowError
        with self.assertRaises(OverflowError):
            power(1e100, 100.0)


class TestInputValidationAndErrorHandling(unittest.TestCase):
    """Test interactive inputs, validations, and recovery."""

    @patch("builtins.input", side_effect=["abc", "18.5"])
    def test_invalid_numeric_input_recovery(self, mock_input):
        """TEST 9: Invalid numeric input displays friendly message and recovers."""
        captured_out = io.StringIO()
        with patch("sys.stdout", captured_out):
            val = get_number("Enter a number: ")
        output = captured_out.getvalue()
        self.assertIn("[ERROR] Invalid input! Please enter a valid number.", output)
        self.assertEqual(val, 18.5)

    @patch("builtins.input", side_effect=["", "   ", "42.0"])
    def test_empty_numeric_input_recovery(self, mock_input):
        """TEST 10: Empty numeric input displays friendly message and recovers."""
        captured_out = io.StringIO()
        with patch("sys.stdout", captured_out):
            val = get_number("Enter a number: ")
        output = captured_out.getvalue()
        self.assertIn("[ERROR] Invalid input! Please enter a valid number.", output)
        self.assertEqual(val, 42.0)

    @patch("builtins.input", side_effect=["9", "7"])
    def test_invalid_menu_selection(self, mock_input):
        """TEST 11: Invalid menu selection displays error and redisplays menu."""
        captured_out = io.StringIO()
        with patch("sys.stdout", captured_out):
            main()
        output = captured_out.getvalue()
        self.assertIn("[ERROR] Invalid selection! Please enter a choice between 1 and 7.", output)
        self.assertIn("Thank you for using the Python CLI Calculator. Goodbye!", output)

    @patch("calculator.get_number", side_effect=[45.0, 0.0])
    def test_division_by_zero_cli_message(self, mock_get_number):
        """TEST 5 CLI: Division by zero displays exact required error message."""
        captured_out = io.StringIO()
        with patch("sys.stdout", captured_out):
            perform_calculation("4")
        output = captured_out.getvalue()
        self.assertIn(
            "[ERROR] Division by zero is undefined! Please enter a non-zero denominator.",
            output,
        )

    @patch("calculator.get_number", side_effect=[10.0, 0.0])
    def test_modulus_by_zero_cli_message(self, mock_get_number):
        """TEST 7 CLI: Modulus by zero displays clear error message without crash."""
        captured_out = io.StringIO()
        with patch("sys.stdout", captured_out):
            perform_calculation("5")
        output = captured_out.getvalue()
        self.assertIn(
            "[ERROR] Modulo by zero is undefined! Please enter a non-zero second operand.",
            output,
        )

    @patch("builtins.input", side_effect=["7"])
    def test_clean_exit(self, mock_input):
        """TEST 13: Option 7 displays exit message and terminates cleanly."""
        captured_out = io.StringIO()
        with patch("sys.stdout", captured_out):
            main()
        output = captured_out.getvalue()
        self.assertIn("Thank you for using the Python CLI Calculator. Goodbye!", output)

    @patch(
        "builtins.input",
        side_effect=[
            # Calculation 1: Addition (10 + 5 = 15)
            "1", "10", "5",
            # Calculation 2: Multiplication (4 * 3 = 12)
            "3", "4", "3",
            # Calculation 3: Division by zero check (45 / 0 -> error)
            "4", "45", "0",
            # Calculation 4: Subtraction (18.5 - 6.5 = 12.0)
            "2", "18.5", "6.5",
            # Calculation 5: Modulus (10 % 3 = 1.0)
            "5", "10", "3",
            # Calculation 6: Power (2 ^ 3 = 8.0)
            "6", "2", "3",
            # Clean Exit
            "7",
        ],
    )
    def test_continuous_execution_multi_operations(self, mock_input):
        """TEST 12: Continuous execution across multiple calculations before exit."""
        captured_out = io.StringIO()
        with patch("sys.stdout", captured_out):
            main()
        output = captured_out.getvalue()

        # Check all results and errors
        self.assertIn("-> Result: 10.00 + 5.00 = 15.00", output)
        self.assertIn("-> Result: 4.00 * 3.00 = 12.00", output)
        self.assertIn("[ERROR] Division by zero is undefined! Please enter a non-zero denominator.", output)
        self.assertIn("-> Result: 18.50 - 6.50 = 12.00", output)
        self.assertIn("-> Result: 10.00 % 3.00 = 1.00", output)
        self.assertIn("-> Result: 2.00 ^ 3.00 = 8.00", output)
        self.assertIn("Thank you for using the Python CLI Calculator. Goodbye!", output)


if __name__ == "__main__":
    unittest.main()
