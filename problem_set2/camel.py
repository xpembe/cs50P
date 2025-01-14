def main() -> None:
    """Main Logic"""

    # Asking the user for a camelCase variable input
    camel_case: str = input("camelCase: ").strip()

    # Converting the camel casing to a snake case
    snake_case: str = to_snake_case(camel_case)
    print("snake_case:", snake_case)


def to_snake_case(camel_case: str) -> str:
    """Taking the camel case variable and return it as snake case"""

    for letter in camel_case:

        # Checking if there's an upper case letter
        if letter.isupper():

            # Taking the index of the upper case letter
            index: int = camel_case.index(letter)

            # Format the string to include the underscore before each uppercase letter
            camel_case = camel_case[:index] + "_" + camel_case[index:]

    return camel_case.lower()  # Convert the string to all lowercase


main()
