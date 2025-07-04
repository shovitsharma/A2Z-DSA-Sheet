# Pattern 8: Print a pyramid of stars
class Solution:
    @staticmethod
    def pattern8(n):
        # Loop through each row
        for i in range(1, n+1):
            # Print spaces for pyramid shape
            for j in range(n-i):
                print(" ", end=" ")
            # Print stars with spaces
            for k in range(2*i-1):
                print("*", end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern8(n)