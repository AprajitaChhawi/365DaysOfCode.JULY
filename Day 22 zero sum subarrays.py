#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        m={}
        c=0
        s=0
        for i in range(n):
            s=s+arr[i]
            if s==0:
                c=c+1
            if s in m:
                c=c+m[s]
            if s not in m:
                m[s]=1
            else:
                m[s]=m[s]+1
        return c
        #return: count of sub-arrays having their sum equal to 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends
