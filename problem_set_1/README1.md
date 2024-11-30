# CS50's Introduction to Python Problem Set 1 from michalpuskac

>This repository contains solutions to several programming challenges written in Python. Each program addresses a unique problem, focusing on topics like string manipulation, mathematical calculations, input validation, and function-based design.

https://cs50.harvard.edu/python/2022/weeks/1/


## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Programs](#how-to-run-the-programs)
---

## What's in This Problem Set

#### 1.	Time-Based Meal Scheduler "Meal Time"
**File**: meal.py

**Problem Description**: This program prompts the user for a time in 24-hour format and outputs whether it’s breakfast, lunch, or dinner time. If the time does not fall within any meal range, it outputs nothing. Meal times are defined as:

 - Breakfast: 7:00–8:00
 - Lunch: 12:00–13:00
 - Dinner: 18:00–19:00

**Code Highlights**

 - Uses a convert function to transform HH:MM time strings into floats for easier comparison.
 - Checks time ranges with if statements to determine meal times.
 - Handles user input and provides meal-based responses based on defined time ranges.

---

#### 2.	Math Interpreter
**File**: interpreter.py

**Problem Description**: This program prompts the user for a simple arithmetic expression (formatted as x y z) and calculates the result as a floating-point number, formatted to one decimal place. The expression includes two integers and an operator (+, -, *, or /).

**Code Highlights**

 - Parses an expression of the form x y z where x and z are integers and y is an operator.
 - Validates input format and operators (+, -, *, /) before calculation.
 - Outputs the result formatted to one decimal place.

#### 3.	File Extension-Based Media Type Identifier "File Extensions"

**File**: extensions.py
**Problem Description**: This program prompts the user for a file name and determines its media type based on the file extension. Supported extensions include .gif, .jpg, .jpeg, .png, .pdf, .txt, and .zip. If the file has an unrecognized or missing extension, it defaults to application/octet-stream.

**Code Highlights**

 - Uses a dictionary to map file extensions to media types, allowing for quick lookups.
 - Extracts the file extension using .rpartition(".") for flexible handling.
 - Outputs a default media type (application/octet-stream) for unknown or missing extensions.


#### 4.	Great Question of Life Interpreter "Deep Thought"
**File**: deep.py

**Problem Description**: This program prompts the user to answer the “Great Question of Life, the Universe, and Everything.” If the user responds with 42, forty-two, or forty two (in any case), the program outputs “Yes.” Otherwise, it outputs “No.”

**Code Highlights**

 - Matches user input (42, forty-two, forty two) to predefined answers using a set for efficient checking.
 - Standardizes input by converting it to lowercase and stripping whitespace.
 - Returns “Yes” for correct answers and “No” for anything else.

#### 5.	Greeting-Based Bank Program "Home Federal Savings Bank"
**File**: bank.py

**Problem Description**: This program prompts the user for a greeting and calculates a dollar amount based on the greeting’s content. The rules are:
 - If the greeting starts with "hello", the program outputs $0.
 - If the greeting starts with "h" but not "hello", it outputs $20.
 - For any other greeting, it outputs $100.

**Code Highlights**

 - Checks if the greeting starts with "hello", starts with "h" but isn’t "hello", or neither.
 - Returns corresponding dollar amounts ($0, $20, $100) based on the greeting content.
 - Uses startswith to make the greeting check efficient and clear.

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
		cd problem_set_1

---

## How to Run the Programs

1. Deep Thought:

        python deep.py

2. Home Federal Savings Bank:

        python bank.py


3. File Extensions:

        python extension.py

4. Math Interpreter:

    	python interpreter.py

5. Meal Time:

        python meal.py

---