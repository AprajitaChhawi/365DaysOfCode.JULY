
#User function Template for python3

class Solution:
    
    #Function to remove common characters and concatenate two strings.
    def concatenatedString(self,s1,s2):
        s=''
        m={}
        l=[]
        for i in s1:
            if i not in m:
                m[i]=1
        for i in s2:
            if i in m:
                m[i]=2
            if i not in m:
                m[i]=1
        for i in s1:
            if m[i]==1:
                s=s+i
        for i in s2:
            if m[i]==1:
                s=s+i
        if len(s)==0:
            return -1
        return s
        
         
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
        print(obj.concatenatedString(s,p))
# } Driver Code Ends
