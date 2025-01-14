def main() -> None:
    """Main Logic"""
    amount_due: int = 50
    coins: list = [25, 10, 5]

    # Keep iterating while amount_due is grater than
    while amount_due > 0:
        # Taking the coin from the user
        coin: int = int(input("Insert coin: "))

        # Checking if the coin is inside coin to proceed
        if coin in coins:
            amount_due = amount_due - coin
        format_report(amount=amount_due)
        continue


def format_report(amount: int) -> None:
    """Printing the formatted output for the amount"""
    print(f"Amount Due: {amount}" if amount > 0 else f"Change Owed: {abs(amount)}")


main()
