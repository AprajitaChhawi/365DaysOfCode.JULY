
#User function Template for python3

class Solution:
    def linear(self,p,m):
        lps=[]
        lps.append(0)
        le=0
        i=1
        while(i<m):
            if p[i]==p[le]:
                lps.append(le+1)
                le=le+1
                i=i+1
            else:
                if le==0:
                    lps.append(0)
                    i=i+1
                else:
                    le=lps[le-1]
        return lps
    #Function to check if the given pattern exists in the given string or not.
    def search(self,p,s):
        m=len(p)
        n=len(s)
        lps=self.linear(p,m)
        i=0
        j=0
        while(i<n):
            if p[j]==s[i]:
                i=i+1
                j=j+1
            if j==m:
                return True
                j=lps[j-1]
            elif(i<n and p[j]!=s[i]):
                if j==0:
                    i=i+1
                else:
                    j=lps[j-1]
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
