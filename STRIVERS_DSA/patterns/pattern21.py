# Pattern 21: Print a hollow square of stars using string multiplication
class solution:
    @staticmethod
    def pattern21(n):
        # Loop through each row
        for i in range(1, n + 1):
            # Print full row of stars for first and last row
            if i == 1 or i == n:
                print('*' * n)
            else:
                # Print star, spaces, then star for middle rows
                print('*' + ' ' * (n - 2) + '*')

num = int(input())
solution.pattern21(num)
