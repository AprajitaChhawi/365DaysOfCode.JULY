#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        m={}
        for i in arr:
            if i in m:
                m[i]=m[i]+1
            else:
                m[i]=1
        for i in arr:
            if m[i]==1:
                return i
        return -1
        # Complete the function


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends
