# Print N times a given string using recursion
class Solution:
    @staticmethod
    def print_N_times(n, s):
        # Base case: if n is 0, stop recursion
        if n == 0:
            return
        # Print the string
        print(s)
        # Recursive call for n-1
        Solution.print_N_times(n-1, s)

n = int(input("Enter N: "))
s = input("Enter string to print: ")
Solution.print_N_times(n, s)