class solution:
    @staticmethod
    def fibonacci(n):
        # Base case: 0 or 1
        if n <= 1:
            return n
        # Recursive case: sum of previous two numbers
        return solution.fibonacci(n-1) + solution.fibonacci(n-2)
    

# Take user input
n = int(input("Enter the position in Fibonacci sequence: "))
# Print the nth Fibonacci number
print("Fibonacci number:", solution.fibonacci(n))