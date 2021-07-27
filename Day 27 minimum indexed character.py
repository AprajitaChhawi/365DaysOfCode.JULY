#User function Template for python3

class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,s, pat): 
        m={}
        n=len(s)
        l=[]
        for i in range(n):
            if s[i] not in m:
                m[s[i]]=i
        for i in pat:
            if i in m:
                l.append(m[i])
        if len(l)==0:
            return -1
        return min(l)
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
        ans = obj.minIndexChar(s,p)
        print(ans)
# } Driver Code Ends
