# Pattern 7: Print a right-angled triangle of stars aligned to the right
class Solution:
    @staticmethod
    def pattern7(n):
        # Loop through each row
        for i in range(1, n+1):
            # Print spaces for right alignment
            for j in range(n-i):
                print(" ", end=" ")
            # Print stars
            for k in range(i):
                print("*", end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern7(n)