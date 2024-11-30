# CS50's Introduction to Python Problem Set 5 from michalpuskac

This repository contains test suites for validating the solutions to problem set 5 from CS50's Introduction to Python. Each problem is focused on improving testing skills using `pytest` and ensuring that code solutions meet the specified requirements.

## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Test Suites](#how-to-run-the-test-suites)

---

## What's in This Problem Set

### 1. **Twttr**
**File**: test_twttr.py

- **Description**: Tests for the `shorten` function, which removes vowels from input strings.

- **Test Cases**:

 - String with vowels only.
 - String with no vowels.
 - Empty string.
 - String with mixed vowels and consonants.

---

### 2. **Bank**
**File**: test_bank.py
- **Description**: Tests for the `process` function, which assigns a monetary value based on the user's input greeting.

- **Test Cases**:

 - Greetings with "hello" (case-insensitive) return 0.
 - Greetings with "hi" or similar phrases return 20.
 - Any other input returns 100.
 - Empty strings return 100.

---

### 3. **Vanity Plate**
**File**: test_plates.py

- **Description**: Tests for the `is_valid` function, which checks the validity of a vanity plate based on specific rules.

- **Test Cases**:

- Valid plates (e.g., "AB123").
- Invalid plates due to length, format, or punctuation.
- Minimum length plates (e.g., "AB").
- Alphanumeric input validity.

---

### 4. **Refueling**
**File**: test_fuel.py

**Description**: Tests for functions related to fuel calculations:
 - `get_fraction`: Parses user input to extract a valid fraction.
 - `calculate_percentage`: Converts a fraction to a percentage.

**Test Cases**:

 - Valid fractions.
 - Invalid fractions handled gracefully.
 - Percentage calculations for various fractions.

---

## Setup and Installation

1. Clone the repository:


        git clone https://github.com/michalpuskac/CS50P-problem-sets.git

### Using a Virtual Environment
It's recmmended keep the project dependencies isolated:
**1. Create a virtual environment:**

	python -m venv venv
or
	python3 -m venv venv

**2. Activate the virtual environment:**

- On Windows:

        .\venv\Scripts\activate

- On macOS/Linux:

        source venv/bin/activate

**3. Install dependencies:**


        pip install -r requirements.txt
        cd problem_set_5

3. Ensure you have Python 3.10 or higher installed.

---

## How to Run the Programs

**To run the tests for all problems:**

        pytest

**To run tests for a specific problem:**

        pytest test_twttr.py

**Replace test_twttr.py with the desired test file name:**
 - test_bank.py
 - test_plates.py
 - test_fuel.py

---