# CS50's Introduction to Python Problem Set 2 from michalpuskac

>This repository contains solutions to various coding problems involving string manipulation, user input validation, and data processing in Python. Each problem has been solved with an emphasis on efficient data handling, user experience, and readability.

## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Test Suites](#how-to-run-the-test-suites)
---

## What's in This Problem Set

#### 1. Camel Case to Snake Case Converter
**File**: camel.py

**Problem Description**: The program prompts the user for a variable name in camel case and converts it to snake case. Camel case uses capital letters to indicate new words (e.g., thisIsCamelCase), while snake case uses underscores (e.g., this_is_snake_case).

**Solution**: We loop through each character in the input string and check if it is uppercase. If it is, we add an underscore (_) before converting it to lowercase, thus achieving the snake case format.

**Code Highlights**

 - String manipulation is used to iterate over the input and conditionally add underscores.
 - Efficiency: The program handles each character only once, resulting in a time-efficient solution.

---

#### 2. Vowel Remover "Just setting up my twttr"
**File**: twttr.py

**Problem Description**: This program is designed to simulate how words are shortened in social media contexts by removing all vowels from a given input string, effectively shortening the text.

**Solution**: Using a generator expression, we filter out any vowel characters (both uppercase and lowercase) from the input string and concatenate the remaining characters.

**Code Highlights**

 - Generator expression for efficient filtering of characters.
 - Set-based lookup for vowels, providing faster membership testing.
 - Case-insensitivity is naturally handled by specifying both uppercase and lowercase vowels in the set.

---

#### 3. Vanity Plate Validator
**File**: plates.py

**Problem Description**: The program prompts the user to input a vanity license plate and checks if it meets specific requirements, such as beginning with at least two letters, having no punctuation, and placing any numbers only at the end without starting with zero.

**Solution**: We divided the problem into separate functions, each handling a specific validation rule, including:
 - Ensuring the plate starts with letters.
 - Checking that the plate has valid length.
 - Confirming numbers (if any) appear only at the end and don’t start with zero.
 - Verifying no punctuation or spaces are present.

**Code Highlights**

 - Modular design with functions for each rule, improving readability and maintainability.
 - Comprehensive validation using logical conditions to enforce multiple constraints.

#### 4. Fruit Calorie Lookup
**File**: nutrition.py

**Problem Description**: The program prompts the user to input a fruit name and outputs the number of calories in one serving of that fruit. The fruit names are matched case-insensitively, and only specific fruits are accepted.

**Solution**: We used a dictionary to store fruit names as keys and their respective calories as values, allowing for quick lookups. The program converts user input to title case to ensure case-insensitive matching with the dictionary keys.

**Code Highlights**

 - Dictionary data structure enables fast, efficient lookups for calorie values.
 - Case normalization using title case to handle various input styles.
 - Error handling to inform the user if the input fruit isn’t in the dataset.

#### 5. Coin Inserter "Coke machine"
**File**: coke.py

**Problem Description**: This program simulates a vending machine that prompts the user to insert coins of specific denominations (5, 10, or 25 cents) until a total of 50 cents is reached. Once the required amount is met, the program outputs any change owed.

**Solution**: The program uses a loop to accumulate the total value of coins entered, while validating that each coin is an acceptable denomination. If the total exceeds 50 cents, the change is calculated and displayed.

**Code Highlights**

 - Loop-based accumulation allows for continuous user input until the required amount is reached.
 - Input validation ensures only accepted coin values are processed.
 - Change calculation displays any excess amount as change after the user meets the target amount.

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
        cd problem_set_2

---

## How to Run the Programs

1. camelCase:

        python camel.py

2. Just setting up my twttr:

        python twttr.py

3. Vanity Plates:

        python plates.py

4. Nutrition Facts:

         python nutrition.py

5. Coke machine:

        python coke.py

6. Bitcoin:

        python bitcoin.py <number_of_bitcoins>

---