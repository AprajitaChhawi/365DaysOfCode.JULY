#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.   
    def ispair(self,arr,l,r,s):
        while(l<r):
            p=arr[l]+arr[r]
            if p==s:
                return True
            elif p>s:
                r=r-1
            else:
                l=l+1
        return False
    def findTriplets(self, arr, n):
        arr.sort()
        for i in range(n):
            if(self.ispair(arr,i+1,n-1,-arr[i])):
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
