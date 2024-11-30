# CS50's Introduction to Python Problem Set 7 from michalpuskac

### 1. Numb3rs Validator
**File**: `numb3rs.py`

**Problem Description**: Implements a program to validate IPv4 addresses. Ensures that the input IP address is in the correct format (x.x.x.x, where each x is between 0 and 255). 

**Solution**: Utilizes regular expressions to check format and boundary values for each segment of the IP address, ensuring it falls within the valid IPv4 range.

**Code Highlights**:
 - Utilizes `re` module to validate the IP address format.
 - Implements boundary checks to ensure numbers fall within the valid IPv4 range.
 - Includes detailed test cases in `test_numb3rs.py` to validate functionality.

### 2. Response Parser
**File**: `response.py`

**Problem Description**: Parses and analyzes responses in text format, with a focus on validating structure and identifying errors.

**Solution**: Extracts specific patterns from input text, processes responses to validate formats, and handles unexpected structures gracefully.

- **Code Highlights**:
 - Includes robust error handling for different response structures.
 - Utilizes Python’s string manipulation techniques for validation and parsing.
 - Easily adaptable for integration with other response processing applications.

### 3. YouTube Embed Link Converter
**File**: `watch.py`

**Problem Description**: Extracts embedded YouTube URLs from HTML, converts them to a short, shareable YouTube URL format (`youtu.be`), ensuring the URL is formatted correctly.

**Solution**: Utilizes regular expressions to locate YouTube embed links within `iframe` tags in HTML and reformats them to their shorter version.

**Code Highlights**:
 - Uses `re.findall` to capture `src` links from HTML iframe elements.
 - Validates and reformats links to short `youtu.be` format.
 - Returns `None` if no valid YouTube URL is found, ensuring clean output for unrelated HTML.

### 4. Time Converter
- **File**: `working.py`

**Problem Description**: Converts time in 12-hour format (with AM/PM) to 24-hour format for consistency and easy processing.

**Solution**: Uses regular expressions to capture time ranges, validates each component, and converts the time to a 24-hour format.

**Code Highlights**:
 - Uses regex to capture and split time components.
 - Converts 12-hour AM/PM format into 24-hour format.
 - Returns an error if the input is invalid or improperly formatted.

**Input**: 9:00 AM to 5:00 PM | 9 AM to 5 PM | 9:00 AM to 5 PM | 9 AM to 5:00 PM
**Output**: 09:00 to 17:00


### 5. "Um" Counter
**File**: `um.py`

**Problem Description**: Counts occurrences of the word "um" in a given text, where it appears as an independent word, case-insensitively.

**Solution**: Uses regular expressions to identify "um" as a standalone word, avoiding matches where "um" is part of another word (like "yummy"). **Code Highlights**:
 - Leverages regex boundaries to count "um" only as a standalone word.
 - Case-insensitive search for flexibility in user input.
 - Includes tests in `test_um.py` to validate various scenarios, such as multiple occurrences, standalone use, and words containing "um."

### 6. Test Files **Files**:
 - `test_numb3rs.py`
 - `test_um.py`
 - `test_working.py`
**Purpose**: Each file contains test functions to verify the accuracy of the respective modules using `pytest`.

**Solution**: Ensures that each function behaves correctly with both valid and invalid inputs, raising appropriate errors or producing expected output.

**Code Highlights**:
 - Implements functions prefixed with `test_` for easy `pytest` discovery.
 - Covers edge cases, expected failures, and typical usage scenarios.
 - Facilitates reliable validation and debugging of core modules.

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

**Run Individual Files**:

1. Numb3rs: try: 255.255.255.255 or 1.2.3.1000 or 'cat'

        numb3rs.py

2. Email Validation:

        response.py

3. Watch on Youtube: try insert embded link from youtube

        watch.py

4. Working 9 to 5.. convert 12-hour format to 24-hour. Expected : 9:00 AM to 5:00 PM, 9:00 AM to 5 PM

        working.py

5. Regular, um, expressions: 'um' word counter

        um.py

**Run Tests**:

 - Run all tests using `pytest` to verify functionality across modules.
 - Command: `pytest` or `pytest test_filename.py` for specific modules.

---
