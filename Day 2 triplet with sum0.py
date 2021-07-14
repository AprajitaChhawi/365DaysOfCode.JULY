#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        m={}
        for i in arr:
            m[i]=1
        for i in range(0,n):
            a=arr[i]
            for j in range(i,n):
                s=a+arr[j]
                k=0-s
                if k in m:
                    return 1
        return 0
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        print(Solution().findTriplets(a,n))
# } Driver Code Ends
