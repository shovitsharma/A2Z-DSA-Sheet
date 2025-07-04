class Solution:
    @staticmethod
    def quick_sort(arr,low,high):
        if low<high:
            pi=Solution.partition(arr,low,high)
            Solution.quick_sort(arr,low,pi-1)
            Solution.quick_sort(arr,pi+1,high)
        else:
            return arr
    @staticmethod
    def partition(arr,low,high):
        pivot=low
        i=low
        j=high
        while i<j:
            while arr[i]<=arr[pivot] and i<=high:
                i+=1
            while arr[j]>arr[pivot] and j>=low:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j

arr=list(map(int,input("Enter the elements of the array: ").split()))
sorted_arr=Solution.quick_sort(arr,0,len(arr)-1)
print("Sorted array:", arr)
