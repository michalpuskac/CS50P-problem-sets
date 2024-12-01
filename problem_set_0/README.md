# CS50's Introduction to Python Problem Set 0 from michalpuskac

>This repository contains a set of beginner-friendly Python exercises designed to reinforce basic programming concepts, string manipulation, and function creation. Each problem includes a small program that prompts the user for input, performs specific transformations or calculations, and outputs the result.

https://cs50.harvard.edu/python/2022/psets/0/


## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Programs](#how-to-run-the-programs)

---

## What's in This Problem Set

#### 1. Lowercase Converter "Indoor Voice"
**File**: indoor.py

**Problem Description**: Prompts the user to enter a string and then outputs the same string in lowercase. Punctuation and whitespace are preserved.

**Key Concepts:** String manipulation, case conversion.

**Example:**
 - **Input**: Hello, World!
 - **Output**: hello, world!

---

#### 2. Space Replacer "Playback Speed"
**File**: playback.py

**Problem Description**: Prompts the user for input and replaces every space with three periods (...). All other characters remain unchanged.

**Key Concepts:** String replacement.

**Example:**
 - **Input**: I love Python
 - **Output**: I...love...Python

#### 3. Emoticon Converter "Making Faces"
**File**: faces.py

**Problem Description**: Converts emoticons :) and :( into their emoji equivalents (🙂 and 🙁). A convert function performs the conversion, while main handles user input and displays the result.

*Key Concepts:* Function creation, string replacement.

*Example*:
**Input**: Hello :) How are you :(
**Output**: Hello 🙂 How are you 🙁

#### 4. Mass-Energy Converter "Einstein"
**File**: einstein.py

**P roblemDescription**: Prompts the user to enter a mass in kilograms and calculates the equivalent energy in Joules using Einstein’s equation,  E = mc^2 .

*Key Concepts:* Constants, basic math operations, formatted output.

*Example*:
 - **Input**: mass = 2 kg
 - **Output**: Equivalent energy (E): 180,000,000,000,000,000 Joules

#### 5. Tip Calculator
**File**: tip.py

**Problem Description**: Converts a dollar amount (formatted as $##.##) to a float and a percentage (formatted as ##%) to a decimal. This allows the program to calculate tips based on a meal cost and tip percentage.

**Functions**:
 - dollars_to_float(): Removes $ and converts the amount to a float.
 - percent_to_float(): Removes %, divides by 100, and returns the decimal form.
 - Key Concepts: String manipulation, basic arithmetic.

*Example*:
 - **Input**:
 - - Meal cost: $50.00
 - - Tip percentage: 15%
 - **Output**: Leave $7.50

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
        cd problem_set_0

---

## How to Run the Programs

1. Indoor Voice:

        python indoor.py

2. Playback Speed:

        python playback.py
 - For a random font:

3. Making Faces:

        python faces.py

4. Einstein:

    python einstein.py

5. Tip Calculator:

        python professor.py

---
