#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        m={}
        for i in range(N):
            if arr[i]==0:
                arr[i]=-1
        maxlen=0
        s=0
        for i in range(N):
            s=s+arr[i]
            if s==0:
                maxlen=max(maxlen,i+1)
            if s in m:
                maxlen=max(maxlen,i-m[s])
            if s not in m:
                m[s]=i
        return maxlen
            
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends
