class Solution:
    @staticmethod
    def pattern2(n):
        # Print a right-angled triangle of stars
        for i in range(1, n+1):
            for j in range(i):
                print("*", end=" ")
            print()  # Newline after each row

# Take user input for the size of the pattern
n = int(input("Enter n: "))
# Print the pattern
Solution.pattern2(n)