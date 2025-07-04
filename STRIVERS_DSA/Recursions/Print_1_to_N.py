# Print numbers from 1 to N using recursion
class Solution:
    @staticmethod
    def Print_1_to_N(n):
        # Base case: if n is 0, stop recursion
        if n == 0:
            return
        # Recursively print numbers up to n-1
        Solution.Print_1_to_N(n-1)
        # Print the current number
        print(n, end=' ')

n = int(input("Enter N: "))
Solution.Print_1_to_N(n)