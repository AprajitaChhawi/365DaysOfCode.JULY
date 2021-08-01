#User function Template for python3


#Function to check if the pattern is present in string or not.
def Rabin_Karp(pat, txt, q):
    d=10
    n=len(txt)
    m=len(pat)
    h=1
    for i in range(0,m-1):
        h=(h*d)%q
    s=0
    t=0
    for i in range(0,m):
        s=(s*d+ord(pat[i]))%q
        t=(t*d+ord(txt[i]))%q
    for i in range(n-m+1):
        if s==t:
            k=0
            for j in range(m):
                if pat[k]!=txt[i+j]:
                    break
                else:
                    k=k+1
            if k==m:
                return True
        if i<n-m:
            t=(d*(t-ord(txt[i])*h)+ord(txt[i+m]))%q
            if t<0:
                t=t+q
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
        txt=str(input())
        pat=str(input())
        q=101
        if(Rabin_Karp(pat,txt,q)):
            print("Yes")
        else:
            print("No")

# } Driver Code Ends
