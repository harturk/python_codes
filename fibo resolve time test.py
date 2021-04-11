"""
Comparation of time to resolve a Fibonacci sequence with memoization and without memoization.
For best results, try entry as 35.
"""
# With memoization
"""memo = {}
def fib(n):
    if n <= 1:
        memo[n] = n
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]"""

# Without memoization
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

s = int(input('Insert an integer value: '))

def main():
    for i in range(s):
        print(i, fib(i))
    print("done")

if __name__ == '__main__':
    main()

