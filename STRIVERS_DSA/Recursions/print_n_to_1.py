# Print numbers from N to 1 using recursion
class Solution:
    @staticmethod
    def print_n_to_1(n):
        # Base case: if n is 0, stop recursion
        if n == 0:
            return
        # Print the current number
        print(n, end=' ')
        # Recursive call for n-1
        Solution.print_n_to_1(n-1)

n = int(input("Enter N: "))
Solution.print_n_to_1(n)