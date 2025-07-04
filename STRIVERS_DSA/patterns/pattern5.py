# Pattern 5: Print an inverted right-angled triangle of stars
class Solution:
    @staticmethod
    def pattern5(n):
        # Loop through each row
        for i in range(n, 0, -1):
            # Print i stars in each row
            for j in range(i):
                print("*", end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern5(n)