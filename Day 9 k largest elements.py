#User function Template for python3

class Solution:
    def heapify(self,arr,n,i):
        largest=i
        left=2*i+1
        right=2*i+2
        if left<n and arr[left]>arr[largest]:
            largest=left
        if right<n and arr[right]>arr[largest]:
            largest=right
        if(largest!=i):
            arr[largest],arr[i]=arr[i],arr[largest]
            self.heapify(arr,n,largest)
    #Function to return k largest elements from an array.
    def kLargest(self,arr,n,k):
        l=[]
        for i in range(n//2 -1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,n-k-1,-1):
            arr[i],arr[0]=arr[0],arr[i]
            l.append(arr[i])
            self.heapify(arr,i,0)
        return l
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends
