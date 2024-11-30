# CS50's Introduction to Python Problem Set 4 from michalpuskac

This repository contains solutions to the problem set 4 from CS50's Introduction to Python. Each program is designed to solve a specific problem, demonstrating skills in Python programming, error handling, and libraries.


## Table of Contents
1. [What's in This Problem Set](#whats-in-this-problem-set)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Programs](#how-to-run-the-programs)

---

## What's in This Problem Set

#### 1. **Emoji**
**File**: emoji.py

**Description**: Converts user input into emoji format using the `emoji` library.

**Input**: Text containing emoji keywords (e.g., `:1st_place_medal:` , `:horse:`, `:Czechia:`).
**Output**: Text with corresponding emoji characters.

---

#### 2. **Figlet**
**File**: figlet.py

**Description**: Creates ASCII art using the `pyfiglet` library.
**Features**:
 - Random font option.
 - Specify font using `-f` or `--font` flag.

**Input**: Text to convert to ASCII art.
**Output**: ASCII art representation.

---

#### 3. **Adieu**
**File**: adieu.py

**Description**: Prompts the user for names, then outputs a grammatically correct farewell message using the `inflect` library.

**Input**: Names entered line by line.
**Output**: "Adieu" message listing all names with correct formatting.

---

#### 4. **Guessing Game**
**File**: guess.py

**Description**: A number guessing game where users try to guess a randomly generated number.

**Features**:
 - User specifies difficulty level.
 - Feedback provided on each guess.

**Input**: Guesses for the number.
**Output**: Feedback on guesses ("Too large", "Too small", or "Just right").

---

#### 5. **Professor**
**File**: professor.py

**Description**: A math quiz generator that challenges the user with addition problems.

**Features**:
 - Supports levels 1, 2, and 3 for difficulty.
 - Up to 3 attempts for each problem.
 - Displays correct answer after failed attempts.

**Input**: Answers to math problems.
**Output**: Feedback and scores.

---

#### 6. **Bitcoin**
**File**: bitcoin.py

**Description**: Calculates the USD value of a specified number of Bitcoins using real-time exchange rates.

**Input**: Number of Bitcoins (via command-line argument).
**Output**: Total value in USD.

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
        cd problem_set_4

---

## How to Run the Programs

1. Emoji:

        python emoji.py

2. Figlet:

        python figlet.py
 - For a random font:

        python figlet.py -f slant
 - For a specific font:

3. Adieu:

        python adieu.py
 - Enter names line by line. Press Ctrl+D (EOF) to finish.

4. Guessing Game:

         python guessing.py

5. Professor:

        python professor.py

6. Bitcoin:

        python bitcoin.py <number_of_bitcoins>

---