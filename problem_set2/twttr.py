# List of english vowels
vowels: list = ["a", "e", "i", "o", "u"]

# Taking the string input from the user
text: str = input("Input: ").strip()

# Iterating over a text string
for letter in text:

    # Checking if letter in vowels
    if letter.lower() in vowels:
        text = text.replace(letter, "")

# Printing the formatted output
print(f"Output: {text}")
