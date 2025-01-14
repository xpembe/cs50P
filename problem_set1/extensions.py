# Asking for a user to input filename
filename: str = input("File name: ")

# Separate the file name from the file extension
splitted_filename: list = filename.split(".")

# Checking for the extension of the file
if filename.endswith(
    (
        ".gif",
        ".jpg",
        ".jpeg",
        ".png",
    )
):
    print(f"image/{splitted_filename[-1]}")
elif "." in filename:
    print(f"Application/{splitted_filename[-1]}")
else:
    print("application/octet_stream")
