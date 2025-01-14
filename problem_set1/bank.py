# Asking for a user to input greeting
greeting: str = input("Greeting: ").strip()

if greeting.lower() == "hello":  # Checking if the user greetings starts with hello
    print("$0")
elif greeting[0].lower() == "h":  # Checking if the user greetings starts with h
    print("$20")
else:  # otherwise
    print("$100")
