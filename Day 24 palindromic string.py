#User function Template for python3
class Solution:
	def isPlaindrome(self, S):
	    n=len(S)
	    low=0
	    high=n-1
	    while(low<=high):
	        if(S[low]!=S[high]):
	            return 0
	        low=low+1
	        high=high-1
	    return 1
	   
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)

# } Driver Code Ends
