#User function Template for python3

class Solution:
    def isPallindrome(self, N):
        stack=[]
        while(N):
            stack.append(N%2)
            N=N//2
        l=0
        r=len(stack)-1
        while(l<=r):
            if stack[l]!=stack[r]:
                return 0
            l=l+1
            r=r-1
        return 1
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isPallindrome(N))
# } Driver Code Ends
