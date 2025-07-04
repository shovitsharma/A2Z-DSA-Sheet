# Pattern 10: Print a triangle of numbers with each row starting from the row number and ending at 1
class Solution:
    @staticmethod
    def pattern10(n):
        # Loop through each row
        for i in range(1, n+1):
            # Print numbers from i down to 1
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern10(n)