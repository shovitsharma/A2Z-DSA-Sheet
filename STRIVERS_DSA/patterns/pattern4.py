class Solution:
    @staticmethod
    def pattern3(n):
        for i in range(1,n+1):
            for j in range(i+1):
                print( i ,end="")
            print()
    # Pattern 4: Print a right-angled triangle of the same number in each row
    @staticmethod
    def pattern4(n):
        # Loop through each row
        for i in range(1, n+1):
            # Print the row number i, i times
            for j in range(i):
                print(i, end=" ")
            print()  # Newline after each row

num = int(input())
Solution.pattern3(num)
Solution.pattern4(num)