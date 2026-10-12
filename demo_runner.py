"""
Interactive Demo and Screenshot Guide Runner.

This script executes each required scenario through the actual calculator
program, displaying genuine terminal output and pausing after each scenario
so you can take clean screenshots for your assignment submission.
"""

import subprocess
import sys


SCENARIOS = [
    {
        "id": "01",
        "filename": "screenshots/01_menu_and_addition.png",
        "title": "Scenario 1: Menu and Addition",
        "description": "Displays the full menu and performs 18.50 + 6.50 = 25.00, then exits.",
        "inputs": "1\n18.5\n6.5\n7\n",
    },
    {
        "id": "02",
        "filename": "screenshots/02_arithmetic_operations.png",
        "title": "Scenario 2: Subtraction, Multiplication, and Division",
        "description": "Performs subtraction (18.5 - 6.5), multiplication (18.5 * 6.5), and division (45 / 5).",
        "inputs": "2\n18.5\n6.5\n3\n18.5\n6.5\n4\n45\n5\n7\n",
    },
    {
        "id": "03",
        "filename": "screenshots/03_division_by_zero.png",
        "title": "Scenario 3: Division by Zero Error",
        "description": "Attempts division with 0 as denominator, showing the exact required error message.",
        "inputs": "4\n45\n0\n7\n",
    },
    {
        "id": "04",
        "filename": "screenshots/04_invalid_input_handling.png",
        "title": "Scenario 4: Invalid Numeric Input and Menu Choice Handling",
        "description": "Tests invalid menu option (9), non-numeric input ('abc'), empty input (''), and recovery.",
        "inputs": "9\n1\nabc\n\n18.5\n6.5\n7\n",
    },
    {
        "id": "05",
        "filename": "screenshots/05_continuous_execution.png",
        "title": "Scenario 5: Modulus, Power, and Continuous Multi-Step Flow",
        "description": "Calculates 10 % 3 = 1.00 and 2 ^ 3 = 8.00 in a continuous session.",
        "inputs": "5\n10\n3\n6\n2\n3\n7\n",
    },
    {
        "id": "06",
        "filename": "screenshots/06_exit_application.png",
        "title": "Scenario 6: Continuous Execution and Clean Application Exit",
        "description": "Shows multiple operations followed by Option 7 clean exit message.",
        "inputs": "1\n10\n5\n7\n",
    },
]


def run_scenario(scenario: dict) -> None:
    print("\n" + "=" * 70)
    print(f"  {scenario['title']}")
    print(f"  File to save: {scenario['filename']}")
    print(f"  Description:  {scenario['description']}")
    print("=" * 70 + "\n")

    # Run the actual calculator.py process with the specified inputs
    proc = subprocess.run(
        [sys.executable, "calculator.py"],
        input=scenario["inputs"],
        text=True,
        capture_output=True,
    )

    # Print the exact output as produced by calculator.py
    print(proc.stdout)

    print("-" * 70)
    print(f"[ACTION] Capture this output using Snipping Tool (Win + Shift + S)")
    print(f"         and save as '{scenario['filename']}'.")
    input("Press Enter to continue to the next scenario...")


def main():
    print("=" * 70)
    print("  PYTHON SIMPLE CALCULATOR - SCREENSHOT CAPTURE COMPANION")
    print("=" * 70)
    print("This script runs calculator.py with genuine inputs for each of the 6")
    print("required screenshot scenarios.")
    input("\nPress Enter to begin...")

    for scenario in SCENARIOS:
        run_scenario(scenario)

    print("\n" + "=" * 70)
    print("All 6 scenarios completed! Ensure all 6 PNG files exist in screenshots/")
    print("=" * 70)


if __name__ == "__main__":
    main()
