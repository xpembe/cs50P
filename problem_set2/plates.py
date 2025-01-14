def main() -> None:
    """Main Logic"""

    # Taking the input plate from the user
    plate: str = input("Plate: ")

    # Checking if the plate is valid or not
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    """Checking if the string s for the plate is valid or invalid"""

    # Checking if the length of s is grater than 2 and less than 6 and
    # checking if the string s contains numbers or alphabets or both and
    # checking if the first two digits of string s is alphabets
    if 2 <= len(s) <= 6 and s.isalnum() and s[:2].isalpha():
        letters: str = "".join(filter(str.isalpha, s))  # Taking all the alphabet values
        numbers: str = "".join(filter(str.isdigit, s))  # Taking all numeric values

        # Checking if numbers exist
        if numbers:

            # Checking if the combination of letters and numbers equal to s and
            # checking if the first number is not equal to 0 and
            # returns the boolean result
            return letters + numbers == s and numbers[0] != "0"

        # If numbers does not exist then check if the combination of
        # letters and numbers equals to s and returns the boolean value
        return letters + numbers == s

    return False


main()
