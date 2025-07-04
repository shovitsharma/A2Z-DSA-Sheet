#count of a digit

"""class Solution:
    @staticmethod
    def countnum(n):
        count=0
        while n>0:
            n=n//10
            count=count+1
        print(count)
    
num = int(input())
Solution.countnum(num)"""

#sum of digits

"""class Solution:
    @staticmethod
    def sumofdigits(n):
        total=0
        while n>0:
            digit = n%10
            total = total+digit
            n = n//10
        print(total)
    
num = int(input())
Solution.sumofdigits(num)"""

#Reverse of a number

class Solution:
    @staticmethod
    def reverse(n):
        while n>0:
            digit=n%10 #to get the last digit
            print(digit)
            n=n//10 #to remove the last digit

num=int(input())
Solution.reverse(num)







        

