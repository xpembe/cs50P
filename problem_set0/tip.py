def main() -> None:
    """Main Logic"""
    dollars: float = dollars_to_float(input("How much was the meal? "))
    percent: float = percent_to_float(input("What percentage would you like to tip? "))
    tip: float = dollars * percent  # Calculating the tip
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d) -> float:
    """Converting the string dollar to a float"""
    format_d: list = d.split("$")  # split string on $ sign
    return float("".join(format_d))  # return the float of the number part


def percent_to_float(p) -> float:
    """Convert the string percentage to a float"""
    percent: int = 100
    format_p: list = p.split("%")  # split string on % sign
    return float("".join(format_p)) / percent  # return the percentage float


main()
