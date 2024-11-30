# CS50's Introduction to Python Problem Set 6 from michalpuskac

This repository contains solutions to problem set 6 from CS50's Introduction to Python. Each program focuses on file handling, data processing, and image manipulation, demonstrating practical applications of Python.

## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Programs](#how-to-run-the-programs)

---

## What's in This Problem Set

### 1. **Lines of Code**
**File**: lines.py

**Description**: Counts the number of lines of actual code in a Python file, ignoring blank lines and comments.

**Usage**:
 - Provide a Python file as input.
 - Outputs the total lines of code excluding comments and blank lines.

**Command**:
        
        python lines.py <filename.py>

---

### 2. **Pizza**
**File**: pizza.py

**Description**: Reads a CSV file and displays its contents in a formatted table using the tabulate library.

**Usage:**
 - Input: A .csv file containing data.
 - Output: A grid-formatted table displayed in the terminal.

**Command**:

        python pizza.py <file.csv>

---

### 3. **Scourgify**
**File**: scourgify.py

**Description**: Reads data from an input CSV file, processes the names into “first, last, house” format, and writes the results to a new CSV file.

**Usage**:
 - Input: A .csv file with name (Last, First) and house fields.
 - Output: A .csv file with separated first, last, and house fields.

**Command**:

        python scourgify.py <input.csv> <output.csv>

---

### 4. **Shirt**
**File**: shirt.py

**Description**: Overlays a transparent shirt image on an input image and saves the result.

**Usage**:
 - Input: An image file (JPG or PNG) to be overlaid.
 - Output: An image file (JPG or PNG) with the shirt overlay applied.

**Requirements:**
The shirt.png overlay file must be in the same directory as the script.

**Command**:

        python shirt.py <input_image> <output_image>

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

General Instructions

1. Each program requires specific inputs as outlined above.
2. Ensure input files (e.g., .csv, images) exist in the same directory or provide the correct file path.
3. Run each program using the provided command in the terminal.

Example Commands

 - Count lines of code:

        python lines.py example.py

 - Display a CSV file as a table:

        python pizza.py menu.csv

 - Convert and process a CSV file, for example included file 'before.csv':

        python scourgify.py input.csv output.csv

 - Overlay a transparent tshirt image over you photo, for example included shirt.png and before3.opng

        python shirt.py <input_image> <output_image>

---