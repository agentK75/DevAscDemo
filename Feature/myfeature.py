def greet(name):
    """Simple greeting function."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == "__main__":
    print(greet("World"))
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"4 is even: {is_even(4)}")