class Solution:
    @staticmethod
    def factorial(n):
        # Base case: factorial of 0 or 1 is 1
        if n == 0 or n == 1:
            return 1
        # Recursive case: n * factorial of (n-1)
        return n * Solution.factorial(n-1)

# Take user input for the number to find factorial of
n = int(input("Enter a number: "))
# Print the factorial of the number
print("Factorial:", Solution.factorial(n))



