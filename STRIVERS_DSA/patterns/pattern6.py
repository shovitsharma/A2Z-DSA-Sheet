# Pattern 6: Print a right-angled triangle of increasing numbers in each row
class Solution:
    @staticmethod
    def pattern6(n):
        # Loop through each row
        for i in range(1, n+1):
            num = 1
            # Print numbers from 1 to i in each row
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern6(n)