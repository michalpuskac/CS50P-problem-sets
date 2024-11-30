"""In a file called extensions.py, implement a program that prompts the user for the name of a file 
and then outputs that file’s media type 
if the file’s name ends, case-insensitively, 
in any of these suffixes: 

".gif" ".jpg." ".jpeg" ".png" ".pdf" '.txt' ".zip"

If the file’s name ends with some other suffix or has no suffix at all, 
output application/octet-stream instead, which is a common default.
"""

# Define a function to retrieve the media type based on the file extension
def get_media_type(file_name):
    # Dictionary to map file extensions to media types
    media_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }
    
    # Extract the file extension in a case-insensitive manner
    _, _, extension = file_name.rpartition(".") #Returns a tuple with three parts: 1.The text before the last, 2.The separator itself ("."), 3.The text after the last .
    extension = extension.lower()

    # Return the media type if found in the dictionary, otherwise return a default
    return media_types.get(extension, "application/octet-stream")


# Define the main function to prompt user input and output the media type
def main():
    file_name = input("What's the file name? ")
    media_type = get_media_type(file_name)
    print(media_type)

if __name__ == "__main__":
    main()