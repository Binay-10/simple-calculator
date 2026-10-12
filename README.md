# Simple Calculator

An interactive, robust command-line calculator written in Python demonstrating core programming fundamentals, input validation, defensive error handling, and continuous loop execution.

---

## 1. Project Title
**Simple Calculator — Interactive Python CLI Application**

---

## 2. Project Overview
The **Simple Calculator** is a modular, menu-driven command-line utility built using Python 3.10+. It enables users to perform standard and advanced arithmetic calculations—including addition, subtraction, multiplication, division, modulus, and exponentiation—within a continuous interactive loop. The program emphasizes defensive programming principles, ensuring that invalid inputs, mathematical singularities (such as division by zero), and arithmetic overflows are intercepted gracefully without application termination or unhandled tracebacks.

---

## 3. Problem Statement
Beginner command-line applications frequently suffer from fragility:
- Non-numeric inputs cause unhandled `ValueError` crashes.
- Division or modulus by zero triggers unhandled `ZeroDivisionError` crashes.
- Execution terminates after a single calculation, requiring tedious manual restarts.
- Arithmetic edge cases (such as float overflows or negative bases with non-integer exponents) produce raw tracebacks, `inf`, `nan`, or complex numbers when real floats are expected.

This project addresses these issues by delivering an intuitive, resilient, and well-structured terminal application adhering to standard software engineering best practices.

---

## 4. Project Objectives
- Implement all core arithmetic operations (`+`, `-`, `*`, `/`, `%`, `**` displayed as `^`).
- Maintain continuous program execution using a controlled `while` loop until explicit user exit.
- Enforce strict input validation using `try...except` exception handling.
- Protect against zero denominators in division and modulus operations.
- Format all numeric results and equations consistently to two decimal places (`.2f`).
- Provide automated unit test coverage using Python's standard `unittest` framework.
- Maintain PEP 8 compliant, readable, and well-documented Python source code.

---

## 5. Features
- **Interactive Menu Interface:** Clear, repeatedly presented numeric menu options (1–7).
- **Graceful Error Recovery:** Non-numeric entries prompt the user to re-enter valid data without crashing or resetting the session.
- **Zero-Division Protection:** Explicit guards and user-friendly error diagnostics for zero denominators.
- **Real-Number Validation:** Complex outputs and float overflows are detected and reported safely.
- **Precision Output:** Inputs and outputs are presented with two decimal places of precision.
- **Clean Termination:** Option 7 or keyboard interrupt signals terminate the program with a polite exit message.

---

## 6. Supported Arithmetic Operations

| Menu Option | Operation | Operator (Python) | Display Symbol | Description | Formula / Example |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | Addition | `+` | `+` | Calculates sum of two numbers | `18.50 + 6.50 = 25.00` |
| **2** | Subtraction | `-` | `-` | Subtracts second number from first | `18.50 - 6.50 = 12.00` |
| **3** | Multiplication | `*` | `*` | Multiplies two numbers | `18.50 * 6.50 = 120.25` |
| **4** | Division | `/` | `/` | Divides numerator by non-zero denominator | `45.00 / 5.00 = 9.00` |
| **5** | Modulus | `%` | `%` | Remainder of division | `10.00 % 3.00 = 1.00` |
| **6** | Power (x^y) | `**` | `^` | Base raised to exponent | `2.00 ^ 3.00 = 8.00` |
| **7** | Exit | N/A | N/A | Terminates application cleanly | Goodbye message |

---

## 7. Technology Stack
- **Language:** Python (v3.10+; tested on Python 3.13.7)
- **Standard Libraries:** `math`, `sys`, `unittest`, `unittest.mock`, `io`
- **External Dependencies:** None (Zero third-party packages required)
- **Supported Platforms:** Windows, macOS, Linux

---

## 8. Python Concepts Demonstrated
- **Variables & Primitive Types:** `float`, `str`, `int`, `bool`.
- **Console I/O:** Reading user input via `input()` and printing formatted output via `print()`.
- **Type Casting & Coercion:** Explicit string-to-float conversion via `float()`.
- **Control Flow:** `if`, `elif`, `else` conditional branching.
- **Repetition & Loops:** `while True` continuous loop execution with `break` and loop control.
- **Exception Handling:** `try...except` handling `ValueError`, `ZeroDivisionError`, `OverflowError`, `KeyboardInterrupt`, and `EOFError`.
- **Mathematical Functions:** `math.isfinite()` verification for floating-point bounds.
- **String Formatting:** Formatted string literals (f-strings) with decimal precision format specifiers (`{value:.2f}`).
- **Modular Architecture:** Pure mathematical functions separated from interactive I/O routines.
- **Automated Testing:** Unit test fixtures, assertions, and mock patches with `unittest`.

---

## 9. Project Folder Structure
```text
simple-calculator/
│
├── calculator.py              # Main application source code
├── README.md                  # Comprehensive project documentation
├── .gitignore                 # Standard Python git ignore rules
│
├── screenshots/               # Terminal execution screenshot evidence
│   ├── 01_menu_and_addition.png
│   ├── 02_arithmetic_operations.png
│   ├── 03_division_by_zero.png
│   ├── 04_invalid_input_handling.png
│   ├── 05_continuous_execution.png
│   └── 06_exit_application.png
│
└── tests/
    └── test_calculator.py     # Automated unit test suite
```

---

## 10. Prerequisites
- **Python 3.10 or higher** installed on your system.
- To verify your Python installation, execute:
  - **Windows (PowerShell/CMD):**
    ```powershell
    python --version
    # or
    py --version
    ```
  - **macOS / Linux:**
    ```bash
    python3 --version
    ```

---

## 11. Installation and Setup
1. Clone the repository or extract the project zip file:
   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd simple-calculator
   ```
2. Verify that all project files are present:
   - Windows PowerShell:
     ```powershell
     Get-ChildItem
     ```
   - Linux / macOS:
     ```bash
     ls -la
     ```
3. No virtual environment or `pip install` commands are needed because the application relies strictly on Python standard libraries.

---

## 12. How to Run the Program
Run the calculator directly using the Python interpreter:

### Windows (PowerShell or Command Prompt)
```powershell
python calculator.py
```
*If using the Windows Python Launcher:*
```powershell
py calculator.py
```

### macOS / Linux
```bash
python3 calculator.py
```

---

## 13. Example Menu and Output

### Menu Interface
```text
=== PYTHON CLI CALCULATOR ===

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Power (x^y)
7. Exit Application

Select Operation (1-7): 1
Enter First Number: 18.5
Enter Second Number: 6.5

-> Result: 18.50 + 6.50 = 25.00
```

### Clean Termination
```text
Select Operation (1-7): 7

Thank you for using the Python CLI Calculator. Goodbye!
```

---

## 14. Input Validation and Error Handling

The application protects against common run-time errors and invalid user inputs:

1. **Non-Numeric and Empty Inputs:**
   - Handled inside `get_number()`.
   - When the user enters strings (e.g. `abc`) or empty whitespace, `float(raw_input)` raises a `ValueError`.
   - The application intercepts this error and displays:
     ```text
     [ERROR] Invalid input! Please enter a valid number.
     ```
   - The prompt repeats until a valid number is provided.

2. **Invalid Menu Choices:**
   - Any selection other than `1` through `7` triggers:
     ```text
     [ERROR] Invalid selection! Please enter a choice between 1 and 7.
     ```
   - The menu is immediately redisplayed.

3. **Division by Zero:**
   - If the user enters a denominator of `0` or `-0.0` for option 4, the operation is blocked before executing division:
     ```text
     [ERROR] Division by zero is undefined! Please enter a non-zero denominator.
     ```

4. **Modulus by Zero:**
   - If the user enters a divisor of `0` or `-0.0` for option 5, the operation is blocked:
     ```text
     [ERROR] Modulo by zero is undefined! Please enter a non-zero second operand.
     ```

5. **Power Operation Edge Cases:**
   - Raising zero to a negative power raises `ZeroDivisionError`:
     ```text
     [ERROR] Zero cannot be raised to a negative power.
     ```
   - Raising a negative base to a fractional exponent generates complex numbers, which is intercepted:
     ```text
     [ERROR] Result is a complex number; real numbers only.
     ```
   - Extreme powers resulting in floating-point overflow raise `OverflowError`:
     ```text
     [ERROR] Calculation overflow! Result is too large to represent.
     ```

6. **Signals and Termination Interrupts:**
   - Pressing `Ctrl+C` (`KeyboardInterrupt`) or `Ctrl+D`/`Ctrl+Z` (`EOFError`) exits gracefully without printing Python tracebacks.

---

## 15. Testing Instructions
The test suite is built on Python's built-in `unittest` framework.

### Run All Tests
Execute test discovery from the project root directory:

#### Windows (PowerShell / CMD)
```powershell
python -m unittest discover -s tests -v
```

#### macOS / Linux
```bash
python3 -m unittest discover -s tests -v
```

### Test Suite Execution Output
```text
test_addition_standard (test_calculator.TestArithmeticOperations.test_addition_standard)
TEST 1: Addition of positive floating-point numbers. ... ok
test_decimal_precision (test_calculator.TestArithmeticOperations.test_decimal_precision)
TEST 14: Decimal precision with fractional values. ... ok
test_division_by_zero (test_calculator.TestArithmeticOperations.test_division_by_zero)
TEST 5: Division by zero raises ZeroDivisionError. ... ok
test_division_standard (test_calculator.TestArithmeticOperations.test_division_standard)
TEST 4: Division with non-zero denominator. ... ok
test_exponentiation_standard (test_calculator.TestArithmeticOperations.test_exponentiation_standard)
TEST 8: Exponentiation calculation. ... ok
test_modulus_by_zero (test_calculator.TestArithmeticOperations.test_modulus_by_zero)
TEST 7: Modulus by zero raises ZeroDivisionError. ... ok
test_modulus_standard (test_calculator.TestArithmeticOperations.test_modulus_standard)
TEST 6: Modulus calculation. ... ok
test_multiplication_standard (test_calculator.TestArithmeticOperations.test_multiplication_standard)
TEST 3: Multiplication of floating-point numbers. ... ok
test_negative_numbers (test_calculator.TestArithmeticOperations.test_negative_numbers)
TEST 15: Arithmetic behavior with negative operands. ... ok
test_non_finite_and_overflow (test_calculator.TestArithmeticOperations.test_non_finite_and_overflow)
TEST 16: Handling overflow and non-finite / complex results. ... ok
test_subtraction_standard (test_calculator.TestArithmeticOperations.test_subtraction_standard)
TEST 2: Subtraction preserving operand order. ... ok
test_clean_exit (test_calculator.TestInputValidationAndErrorHandling.test_clean_exit)
TEST 13: Option 7 displays exit message and terminates cleanly. ... ok
test_continuous_execution_multi_operations (test_calculator.TestInputValidationAndErrorHandling.test_continuous_execution_multi_operations)
TEST 12: Continuous execution across multiple calculations before exit. ... ok
test_division_by_zero_cli_message (test_calculator.TestInputValidationAndErrorHandling.test_division_by_zero_cli_message)
TEST 5 CLI: Division by zero displays exact required error message. ... ok
test_empty_numeric_input_recovery (test_calculator.TestInputValidationAndErrorHandling.test_empty_numeric_input_recovery)
TEST 10: Empty numeric input displays friendly message and recovers. ... ok
test_invalid_menu_selection (test_calculator.TestInputValidationAndErrorHandling.test_invalid_menu_selection)
TEST 11: Invalid menu selection displays error and redisplays menu. ... ok
test_invalid_numeric_input_recovery (test_calculator.TestInputValidationAndErrorHandling.test_invalid_numeric_input_recovery)
TEST 9: Invalid numeric input displays friendly message and recovers. ... ok
test_modulus_by_zero_cli_message (test_calculator.TestInputValidationAndErrorHandling.test_modulus_by_zero_cli_message)
TEST 7 CLI: Modulus by zero displays clear error message without crash. ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.004s

OK
```

---

## 16. Sample Test Cases and Expected Results

| Test ID | Category | Inputs | Expected Output / Behavior | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TEST 1** | Addition | `18.5` and `6.5` | `-> Result: 18.50 + 6.50 = 25.00` | PASSED |
| **TEST 2** | Subtraction | `18.5` and `6.5` | `-> Result: 18.50 - 6.50 = 12.00` | PASSED |
| **TEST 3** | Multiplication | `18.5` and `6.5` | `-> Result: 18.50 * 6.50 = 120.25` | PASSED |
| **TEST 4** | Division | `45` and `5` | `-> Result: 45.00 / 5.00 = 9.00` | PASSED |
| **TEST 5** | Division by Zero | `45` and `0` | `[ERROR] Division by zero is undefined! Please enter a non-zero denominator.` | PASSED |
| **TEST 6** | Modulus | `10` and `3` | `-> Result: 10.00 % 3.00 = 1.00` | PASSED |
| **TEST 7** | Modulus by Zero | `10` and `0` | `[ERROR] Modulo by zero is undefined! Please enter a non-zero second operand.` | PASSED |
| **TEST 8** | Exponentiation | `2` and `3` | `-> Result: 2.00 ^ 3.00 = 8.00` | PASSED |
| **TEST 9** | Non-Numeric Input | `abc` | `[ERROR] Invalid input! Please enter a valid number.` (re-prompt) | PASSED |
| **TEST 10** | Empty Input | `""` (Enter) | `[ERROR] Invalid input! Please enter a valid number.` (re-prompt) | PASSED |
| **TEST 11** | Invalid Menu Choice | `9` | `[ERROR] Invalid selection! Please enter a choice between 1 and 7.` | PASSED |
| **TEST 12** | Continuous Execution | Sequence of operations | Menu repeats automatically after each operation | PASSED |
| **TEST 13** | Exit Application | `7` | `Thank you for using the Python CLI Calculator. Goodbye!` | PASSED |
| **TEST 14** | Decimal Precision | `0.1` and `0.2` | `-> Result: 0.10 + 0.20 = 0.30` | PASSED |
| **TEST 15** | Negative Numbers | `-5.0` and `-3.0` | `-> Result: -5.00 + -3.00 = -8.00` | PASSED |
| **TEST 16** | Overflow / Non-Finite | `1e100` and `100` | Handled via `OverflowError` message | PASSED |

---

## 17. Screenshots Section

Genuine screenshots of interactive terminal execution are cataloged in the [`screenshots/`](screenshots/) directory.

| File | Scenario Description |
| :--- | :--- |
| [`01_menu_and_addition.png`](screenshots/01_menu_and_addition.png) | Calculator header, complete menu display, and successful addition (`18.5 + 6.5 = 25.00`). |
| [`02_arithmetic_operations.png`](screenshots/02_arithmetic_operations.png) | Successful subtraction, multiplication, and non-zero division calculations. |
| [`03_division_by_zero.png`](screenshots/03_division_by_zero.png) | Division-by-zero attempt and the exact required error diagnostic message. |
| [`04_invalid_input_handling.png`](screenshots/04_invalid_input_handling.png) | Non-numeric input (`abc`), empty input handling, and out-of-range menu selection (`9`). |
| [`05_continuous_execution.png`](screenshots/05_continuous_execution.png) | Modulus (`10 % 3`), exponentiation (`2 ^ 3`), and continuous multi-step calculation flow. |
| [`06_exit_application.png`](screenshots/06_exit_application.png) | Multi-operation session concluding with option `7` and clean termination message. |

> **Note on Submission Evidence:**
> If you are setting up or re-capturing screenshots on your local workstation, run the application in your terminal (`python calculator.py`), execute the relevant test steps, use the Windows Snipping Tool (`Win + Shift + S`) or macOS screenshot shortcut (`Cmd + Shift + 4`), and save the files with the matching filenames into the `screenshots/` directory.

---

## 18. Learning Outcomes
- Understanding the complete lifecycle of a command-line application in Python.
- Applying defensive programming through targeted `try...except` exception handling.
- Structuring clean, maintainable functions adhering to PEP 8 standards.
- Managing interactive application states and repetition via `while` loops.
- Designing and implementing automated test suites using `unittest` and `unittest.mock`.
- Configuring proper version control workflows with Git and GitHub.

---

## 19. Limitations
- **Console Interface Only:** The application operates strictly within a text terminal and does not provide a graphical user interface (GUI) or web interface.
- **Two Operands Per Step:** Each calculation accepts two numbers at a time rather than evaluating arbitrary multi-operator algebraic expressions (e.g. `2 + 3 * 4`).
- **Real Float Domain:** Calculations are constrained to real numbers; complex numbers resulting from negative bases with fractional exponents are intentionally rejected.

---

## 20. Future Enhancements
- Adding calculation history tracking allowing users to review prior results in the current session.
- Implementing memory functions (`M+`, `M-`, `MR`, `MC`).
- Expanding scientific functions such as square root (`sqrt`), logarithm (`log`), and trigonometric functions (`sin`, `cos`, `tan`).
- Supporting multi-operand expression parsing using an abstract syntax tree (AST) or Shunting-yard algorithm.

---

## 21. Author Information
- **Author:** [Your Name / Student Name]
- **Course / Assignment:** Python Programming — Simple Calculator Assignment
- **Institution:** [Your Institution / University]
- **Date:** October 2026

---

## 22. License
This project is open-source and released under the **MIT License**. You are free to study, modify, and distribute this software for educational and personal purposes.
