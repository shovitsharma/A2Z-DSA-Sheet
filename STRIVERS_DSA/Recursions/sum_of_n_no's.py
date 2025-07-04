# Find the sum of first n natural numbers using recursion
class Solution:
    @staticmethod
    def sum_of_n_numbers(n):
        # Base case: if n is 0, return 0
        if n == 0:
            return 0
        # Recursive case: n + sum of numbers up to n-1
        return n + Solution.sum_of_n_numbers(n-1)

n = int(input("Enter n: "))
print("Sum:", Solution.sum_of_n_numbers(n))