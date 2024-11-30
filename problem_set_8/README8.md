# CS50's Introduction to Python Problem Set 8 from michalpuskac

This repository contains solutions to problem set 8 from CS50's Introduction to Python. Each program explores the use of Object-Oriented Programming (OOP) concepts in Python to solve practical problems.

## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Programs](#how-to-run-the-programs)

---

## What's in This Problem Set

### 1. **Jar**
**File**: jar.py

**Description**: Simulates a cookie jar with specified capacity. Allows depositing and withdrawing cookies while respecting capacity limits.

**Usage**:
 - Create a `Jar` object with a given capacity.
 - Use methods `deposit`, `withdraw`, and properties `size` and `capacity` to interact with the jar.

**Example**:

		jar = Jar(10)
		jar.deposit(5)
		print(jar)  # Outputs: 🍪🍪🍪🍪🍪
		jar.withdraw(2)
		print(jar.size)  # Outputs: 3

### 2. Seasons

**File:** seasons.py

**Description:** Calculates the number of minutes a person has lived based on their date of birth and converts the result to words.

**Usage**:
 - **Input**: A birth date in YYYY-MM-DD format.
 - **Output**: The total minutes lived, written in words.

**Command:**

    	python seasons.py

**Example:**

		Date of birth YYYY-MM-DD: 2000-01-01
		one million fifty-two thousand five hundred sixty minutes.

### 3. Shirtificate

**File**: shirtificate.py

**Description**: Generates a “shirtificate” PDF with a personalized message and shirt image. The program uses the FPDF library for PDF creation.

**Usage**:
 - Input: Name to appear on the shirtificate.
 - Output: A PDF file named shirtificate.pdf.

**Requirements**:
 - The shirtificate.png image file must be in the same directory.

**Command**:

    	python shirtificate.py

**Example**:

		Name: <your name>
		Shirtificate created successfully!

---

### 4. Testing

**Jar Tests**

File: test_jar.py

**Description**: Unit tests for the Jar class, validating capacity, deposit, withdrawal, and string representation.

**Seasons Tests**

**File**: test_seasons.py

**Description**: Unit tests for functions in seasons.py to ensure correct calculation of minutes lived and conversion to words.

**Usage**:
Run the tests using pytest:

		pytest test_jar.py
		pytest test_seasons.py

---

## Setup and Installation

1. Clone the repository:

        git clone https://github.com/michalpuskac/CS50P-problem-sets.git

### Using a Virtual Environment

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
        cd problem_set_6

---

## How to Run the Programs

	1.	Follow the usage instructions for each program.
	2.	Ensure any required files (e.g., shirtificate.png) are in the same directory as the program.
	3.	Run each program using the provided command in the terminal.

### Example Commands

 - Run the Jar simulation:
		python jar.py

 - Calculate minutes lived:
		python seasons.py

 - Generate a shirtificate:
		python shirtificate.py

 - Run tests:

		pytest test_jar.py
		pytest test_seasons.py

---

Notes

 - Ensure that shirtificate.png exists in the same directory as shirtificate.py for proper execution.