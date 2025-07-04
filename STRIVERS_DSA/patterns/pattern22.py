# Pattern 22: Print a cross (X) pattern of stars
class Solution:
    @staticmethod
    def pattern22(n):
        # Loop through each row
        for i in range(n):
            for j in range(n):
                # Print star at the diagonals
                if i == j or i + j == n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern22(n)
