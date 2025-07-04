# Pattern 20: Print a hollow square of stars
class Solution:
    @staticmethod
    def pattern20(n):
        # Loop through each row
        for i in range(n):
            for j in range(n):
                # Print star at the border, space inside
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern20(n)
