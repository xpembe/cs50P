def main() -> None:
    """Main Logic"""

    # Asking the user for the present time
    time_str: str = input("What time is it? ").strip()
    time: float = convert(time_str)

    # printing appropriate meal according to their time
    if 7.00 <= time <= 8.00:
        print("Breakfast time")

    if 12.00 <= time <= 13.00:
        print("Launch time")

    if 18.00 <= time <= 19.00:
        print("Dinner time")


def convert(time: str) -> float:
    """Convert string time to a decimal time"""

    # Return the decimal time
    return float(time.replace(":", "."))


if __name__ == "__main__":
    main()
