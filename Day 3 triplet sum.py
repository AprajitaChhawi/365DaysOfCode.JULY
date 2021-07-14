#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def ispair(self,A,l,r,s):
        while(l<r):
            p=A[l]+A[r]
            if p==s:
                return True
            elif p>s:
                r=r-1
            else:
                l=l+1
        return False
    def find3Numbers(self,A, n, X):
        A.sort()
        for i in range(0,n):
            if (self.ispair(A,i+1,n-1,X-A[i])):
                return 1
        return 0
        # Your Code Here

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
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
