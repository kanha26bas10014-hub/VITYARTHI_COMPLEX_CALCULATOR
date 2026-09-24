# Complex Calculator

A simple command-line calculator built in Python. It supports addition, subtraction, multiplication, division (on a list of numbers), and exponentiation.

## Features

- **Add / Subtract / Multiply / Divide** — enter as many numbers as you like, one at a time, and get the combined result.
- **Exponential** — raise a number to a given power.
- Basic input validation (invalid numbers, empty input, and division by zero are handled gracefully).
- Runs in a loop so you can perform multiple calculations without restarting the program.

## Prerequisites

- **Python 3.6 or higher** installed on your system.
  - Check your version with:
    ```bash
    python3 --version
    ```
  - If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

## Dependencies

This project uses **only Python's standard library** — no external packages are required, and no `pip install` step is necessary.

## Setup Instructions

1. **Get the code**
   - Clone the repository, or simply download the file `vityarthi_pro1.py` to a folder on your computer.

2. **Open a terminal / command prompt**
   - Navigate to the folder containing the file:
     ```bash
     cd path/to/your/folder
     ```

3. **(Optional) Rename the file**
   - The file may currently be named with a space (e.g. `vityarthi pro1.py`). If your system has trouble with spaces in filenames, rename it to `vityarthi_pro1.py` (underscore instead of space).

4. No further configuration or environment variables are needed.

## Running the Program

Run the script using Python 3:

```bash
python3 vityarthi_pro1.py
```

On Windows, you may instead use:

```bash
python vityarthi_pro1.py
```

## How to Use

When the program starts, you'll see a menu:

```
------WELCOME------
To add,substract, multiply and divide--Enter: 0
For exponential-- Enter: 1
To exit-- Enter 2
enter your choice:
```

### Option 0 — Add / Subtract / Multiply / Divide
1. Enter `0` at the main menu.
2. Choose an operation: `+`, `-`, `*`, `/`, or `q` to go back.
3. Enter numbers one at a time when prompted.
4. Type `E` or `e` when you're done entering numbers to see the result.
5. The result is printed, and you're returned to the operation menu.

**Example:**
```
enter your choice: 0
operations: add[+] substract[-] multiply[*]  divide[/] quit[q]
enter your choice: +
enter number one by one
type 'E' or 'e' to exit the calculator
Enter a number(or 'E' to exit)5
Enter a number(or 'E' to exit)10
Enter a number(or 'E' to exit)E
result= 15.0
```

### Option 1 — Exponential
1. Enter `1` at the main menu.
2. Enter the base number.
3. Enter the power/exponent.
4. The result (base ^ power) is printed.

**Example:**
```
enter your choice: 1
enter the number: 2
enter the power: 3
result: 8.0
```

### Option 2 — Exit
- Enter `2` to display a thank-you message. Note: the main loop currently continues after this; to fully stop the program, close the terminal or press `Ctrl+C`.

## Error Handling

- **Invalid menu choice**: Prompts you to enter a valid option.
- **Invalid operation symbol**: Prompts "invalid input" and asks again.
- **Non-numeric input**: Prints "Error: Invalid input" and asks you to re-enter the number.
- **No numbers entered**: Prints "Error: no number was entered."
- **Division by zero**: Prints "Error: can't divide by 0."
- **Invalid number for exponential**: Prints "Error: Please enter valid number".

## Stopping the Program

Since the program runs in an infinite loop, you can stop it at any time by pressing:

```
Ctrl+C
```

in the terminal.

## Project Structure

```
.
├── vityarthi_pro1.py   # Main calculator script
└── README.md           # Project documentation (this file)
```
