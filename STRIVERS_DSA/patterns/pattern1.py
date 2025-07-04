class Solution:
    @staticmethod
    def pattern1(n):
        # Print a square of n x n stars
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()  # Newline after each row

# Take user input for the size of the pattern
n = int(input("Enter n: "))
# Print the pattern
Solution.pattern1(n)