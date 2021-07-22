#User function Template for python3

class Solution:
    def findSubarraySum(self,arr, n, Sum):  
        m={}
        count=0
        s=0
        for i in range(n):
            s=s+arr[i]
            if Sum==s:
                count=count+1
            if s-Sum in m:
                count=count+m[s-Sum]
            if s not in m:
                m[s]=1
            else:
                m[s]=m[s]+1
        return count
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=int(input())
    ob = Solution()
    print(ob.findSubarraySum(a, n, s))
    
# } Driver Code Ends
