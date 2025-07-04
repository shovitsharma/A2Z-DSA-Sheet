# Pattern 11: Print a binary triangle pattern
class Solution:
    @staticmethod
    def pattern11(n):
        # Loop through each row
        for i in range(1, n+1):
            # Print 1 and 0 alternately in each row
            for j in range(1, i+1):
                print((i+j)%2, end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern11(n)