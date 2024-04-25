def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        fibonacci_recursive(n - 1) +fibonacci_recursive(n - 2)