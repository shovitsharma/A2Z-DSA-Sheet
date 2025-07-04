# Pattern 19: Print a diamond of stars
class Solution:
    @staticmethod
    def pattern19(n):
        # Upper part of the diamond
        for i in range(n):
            print(" " * (n-i-1) + "* " * (i+1))
        # Lower part of the diamond
        for i in range(n-2, -1, -1):
            print(" " * (n-i-1) + "* " * (i+1))

n = int(input("Enter n: "))
Solution.pattern19(n)
