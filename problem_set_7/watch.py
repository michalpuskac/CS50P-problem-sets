"""
Implement a function called parse that expects a str of HTML as input,
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
and returns its shorter, shareable youtu.be equivalent as a str.
Expect that any such URL will be in one of the formats below.
Assume that the value of src will be surrounded by double quotes.
And assume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None.
- http://youtube.com/embed/xvFZjo5PgG0
- https://youtube.com/embed/xvFZjo5PgG0
- https://www.youtube.com/embed/xvFZjo5PgG0

input: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
output: https://youtu.be/xvFZjo5PgG0
"""
import re 
import sys


def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    #search for the pattern in the input string (s)
    match = re.search(pattern, s)

    if match:
        #Extract the video ID
        video_id = match.group(1)
        #Return the shortened URL
        return f"https://youtu.be/{video_id}"

    #If no match return None
    return None

def main():
    print(parse(input("HTML: ")))

if __name__ == "__main__":
    main()