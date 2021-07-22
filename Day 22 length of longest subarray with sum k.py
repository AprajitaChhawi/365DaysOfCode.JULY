#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        m={}
        maxlen=0
        s=0
        for i in range(N):
            s=s+A[i]
            if s==K:
                maxlen=max(maxlen,i+1)
            elif s-K in m:
                maxlen=max(maxlen,i-m[s-K])
            if s not in m:
                m[s]=i
        return maxlen
        #Complete the function
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends
