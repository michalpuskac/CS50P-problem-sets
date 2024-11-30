# CS50's Introduction to Python Problem Set 3 from michalpuskac

>This repository contains solutions to four Python exercises, focusing on parsing input, handling errors, and formatting outputs.

https://cs50.harvard.edu/python/2022/weeks/3/


## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Programs](#how-to-run-the-programs)

---

## What's in This Problem Set

#### 1. Fuel Gauge
**File**: fuel.py

**Problem Description**: This program calculates the fuel percentage from a fraction (X/Y) and displays the remaining fuel as a percentage. If the tank is nearly empty (1% or less), it displays E, and if almost full (99% or more), it displays F.

**Code Highlights**

 - Exception Handling: Catches invalid inputs (ValueError, ZeroDivisionError).
 - Looping: Prompts until a valid fraction is entered.
 - Edge Cases: Checks if fuel is <= 1% or >= 99%.

---

#### 2. Grocery List
**File**: grocery.py

**Problem Description**: The program collects items for a grocery list, counting each item’s occurrences. When the user inputs control-d, it displays the list in uppercase, sorted alphabetically, with each item prefixed by the count.

**Code Highlights**

 - Dictionary: Stores item counts.
 - Sorting and Formatting: Outputs items in uppercase, sorted with count prefixes.

#### 3. Date Formatter "Outdated"
**File**: outdated.py

**Problem Description**: This program accepts dates in two formats (MM/DD/YYYY and Month DD, YYYY) and outputs them in ISO format (YYYY-MM-DD). It handles case insensitivity and validates basic date structure.

**Code Highlights**

 - Parsing: Handles both numeric and textual month formats.
 - Date Formatting: Converts dates to ISO format.
 - Exception Handling: Validates dates and prompts again for incorrect formats.

#### 4. Ordering Menu "Felipe's Taqueira"
**File**: taqueria.py

**Problem Description**: A simple ordering program that allows the user to input menu items one at a time. The program displays the cumulative cost after each item and allows the user to exit by typing "quit" or pressing control-d.

**Code Highlights**

 - Dictionary: Stores menu items and their prices.
 - Error Handling: Catches EOFError for control-d.
 - Case Insensitivity: Handles item names without case sensitivity.

---

## Setup and Installation

1. Clone the repository:

        git clone https://github.com/michalpuskac/CS50P-problem-sets.git

2### Using a Virtual Environment
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
		cd problem_set_3

---

## How to Run the Programs

1. Fuel Gauge:

        python fuel.py

2. Grocery List:

        python grocery.py


3. Date Formater "Oudated":

        python outdated.py

4. Ordering Menu "Felipe's Taqueira":

    	python taqueira.py

---