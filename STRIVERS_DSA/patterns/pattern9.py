class Solution:
    @staticmethod 
    def pattern9(n):
        # Loop through each row
        for i in range(1, n+1):
            # Print numbers from 1 to i
            for j in range(1, i+1):
                print(j, end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern9(n)