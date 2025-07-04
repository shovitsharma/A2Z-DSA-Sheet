# Pattern 17: Print a pyramid of letters
class Solution:
    @staticmethod
    def pattern17(n):
        # Loop through each row
        for i in range(n):
            # Print spaces for pyramid shape
            for j in range(n-i-1):
                print(" ", end="")
            # Print letters increasing up to the middle
            for j in range(i+1):
                print(chr(65+j), end="")
            # Print letters decreasing after the middle
            for j in range(i-1, -1, -1):
                print(chr(65+j), end="")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern17(n)