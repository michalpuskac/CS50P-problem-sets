"""
implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""
def get_media_type(file_name):

        file_extension = file_name.casefold().split(".")[-1] if "." in file_name else None  

        if file_extension == "gif":                             
                return "image/gif"                              
        elif file_extension == "jpg":
                return "image/jpeg"
        elif file_extension == "jpeg":
                return "image/jpeg"
        elif file_extension == "png":
                return "image/png"
        elif file_extension == "pdf":
                return "application/pdf"
        elif file_extension == "txt":
                return "text/plain"
        elif file_extension == "zip":
                return "application/zip"
        else:                                                  
                return "application/octet-stream"


def main():
        file_name = input("What's file name? " )
        media_type = get_media_type(file_name)
        print(f"{media_type}")

if __name__ == "__main__":
    main()

