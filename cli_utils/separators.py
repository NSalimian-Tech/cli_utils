def print_separator():
    """Prints a green line of stars."""
    print("\033[32m" + "*" * 30 + "\033[0m")

def print_box(message):
    """Prints a message inside a yellow ASCII box."""
    yellow = "\033[33m"
    reset = "\033[0m"
    length = len(message)
    print(f"{yellow}+{'-' * (length + 2)}+")
    print(f"| {message} |")
    print(f"+{'-' * (length + 2)}+{reset}")