
#User function Template for python3


class Solution:
    
    #Function to check if the given pattern exists in the given string or not.
    def search(self,p,s):
        n=len(s)
        m=len(p)
        i=0
        for i in range(n-m+1):
            k=0
            for j in range(m):
                if s[i+j]!=p[k]:
                    break
                k=k+1
            if k==m:
                return True
        return False
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
        s=str(input())
        p=str(input())
        obj = Solution()
        if(obj.search(p,s)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
