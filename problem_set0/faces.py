def main() -> None:
    """Main Logic"""

    # Asking for a user to input something
    user_input: str = input()

    # Displaying the user input with actual emoji
    print(convert(user_input))


def convert(input: str) -> str:
    """Convert string to an appropriate emoji"""

    # replacing :) and :( emotions with 🙂 and 🙁 emoji respectively
    input = "🙂".join(input.split(":)"))
    input = "🙁".join(input.split(":("))

    return input


main()
