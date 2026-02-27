import math
import logging
print("WEBHOOK TRIGGER CHECK!!!")
# ── Logging setup ──────────────────────────────────────────────────────────────
# Logs are written to calculator.log (used later by ELK stack for monitoring)
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ── Core calculator functions ──────────────────────────────────────────────────

def square_root(x):
    """Returns √x. Raises error for negative input (no real square root)."""
    if x < 0:
        raise ValueError(f"Cannot compute square root of a negative number: {x}")
    result = math.sqrt(x)
    logging.info(f"square_root({x}) = {result}")
    return result

def factorial(x):
    """Returns x! Only valid for non-negative integers."""
    if not isinstance(x, int) or x < 0:
        raise ValueError(f"Factorial is only defined for non-negative integers: {x}")
    result = math.factorial(x)
    logging.info(f"factorial({x}) = {result}")
    return result

def natural_log(x):
    """Returns ln(x). Only valid for x > 0."""
    if x <= 0:
        raise ValueError(f"Natural log is only defined for positive numbers: {x}")
    result = math.log(x)
    logging.info(f"natural_log({x}) = {result}")
    return result

def power(x, b):
    """Returns x^b."""
    result = math.pow(x, b)
    logging.info(f"power({x}, {b}) = {result}")
    return result

# ── Menu-driven interface ──────────────────────────────────────────────────────

def display_menu():
    print("\n=============================")
    print("    Scientific Calculator    ")
    print("=============================")
    print("1. Square Root  √x")
    print("2. Factorial    x!")
    print("3. Natural Log  ln(x)")
    print("4. Power        x^b")
    print("5. Exit")
    print("=============================")

def main():
    logging.info("Calculator application started")
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                x = float(input("Enter x: "))
                print(f"Result: √{x} = {square_root(x)}")

            elif choice == "2":
                x = int(input("Enter x (non-negative integer): "))
                print(f"Result: {x}! = {factorial(x)}")

            elif choice == "3":
                x = float(input("Enter x (must be > 0): "))
                print(f"Result: ln({x}) = {natural_log(x)}")

            elif choice == "4":
                x = float(input("Enter base x: "))
                b = float(input("Enter exponent b: "))
                print(f"Result: {x}^{b} = {power(x, b)}")

            elif choice == "5":
                print("Goodbye!")
                logging.info("Calculator application exited by user")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                logging.warning(f"Invalid menu choice entered: {choice}")

        except ValueError as e:
            print(f"Error: {e}")
            logging.error(f"ValueError: {e}")

if __name__ == "__main__":
    main()