
class Solution:
    def merge(self,A,B):
        l=[]
        n1=len(A)
        n2=len(B)
        i=0
        j=0
        while(i<n1 and j<n2):
            if A[i]<B[j]:
                l.append(A[i])
                i=i+1
            elif A[i]>B[j]:
                l.append(B[j])
                j=j+1
            else:
                l.append(A[i])
                l.append(A[i])
                i=i+1
                j=j+1
        while(i<n1):
            l.append(A[i])
            i=i+1
        while(j<n2):
            l.append(B[j])
            j=j+1
        return l
            #User function Template for python3
    #Function to merge three sorted arrays into a single array.
    def mergeThree(self, A,B,C):
        l1=self.merge(A,B)
        l2=self.merge(l1,C)
        return l2#code here

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
        n,m,p = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        C = list(map(int, input().strip().split()))
        obj = Solution()
        print(*obj.mergeThree(A,B,C))
# } Driver Code Ends
