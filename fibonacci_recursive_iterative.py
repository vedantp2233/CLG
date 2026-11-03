# Fibonacci using Recursion
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Fibonacci using Iteration
def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("Enter number of terms: "))

print("\nRecursive Fibonacci:")
for i in range(n):
    print(fib_recursive(i), end=" ")

print("\n\nNon-Recursive Fibonacci:")
fib_iterative(n)
