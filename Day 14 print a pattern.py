#User function Template for python3
class Solution:
	def printPattern(self, N):
	    top=0
        bottom=2*N-2
        left=0
        right=2*N-2
	    for i in range(2*N-1):
	        for j in range(2*N-1):
	            if i==0 or j==0 or i==2*N-2 or j==2*N-2:
	                print(N,end=" ")
	            else:
	                print(N-min(i-top,j-top,bottom-i,bottom-j,right-i,right-j,i-left,j-left),end=" ")
	                # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ob.printPattern(N)

# } Driver Code Ends
