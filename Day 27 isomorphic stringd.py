#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        m1={}
        m2={}
        for i in str1:
            if i in m1:
                m1[i]=m1[i]+1
            else:
                m1[i]=1
        for i in str2:
            if i in m2:
                m2[i]=m2[i]+1
            else:
                m2[i]=1
        k=len(m1)
        l=len(m2)
        if k!=l:
            return False
        for i in range(k):
            if m1[str1[i]]!=m2[str2[i]]:
                return False
        return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
