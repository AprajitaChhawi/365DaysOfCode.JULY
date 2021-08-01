
#User function Template for python3

class Solution:
    
    #Function to find minimum number of characters which Ishaan must insert  
    #such that string doesn't have three consecutive same characters.
    def modified(self,s):
        count=0
        n=len(s)
        i=0
        while(i<n-2):
            if s[i]==s[i+1] and s[i+1]==s[i+2]:
                i=i+2
                count=count+1
            else:
                i=i+1
        return count
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
        obj = Solution()
        print(obj.modified(s))
# } Driver Code Ends
