#User function Template for python3

class Solution:
	def BoundaryElements(self, matrix):
	    n=len(matrix)
	    l=[]
	    for i in range(n):
	        if i==0 or i==n-1:
	            for j in range(n):
	                l.append(matrix[i][j])
	        else:
	            l.append(matrix[i][0])
	            l.append(matrix[i][n-1])
	    return l
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		ob = Solution()
		ans = ob.BoundaryElements(matrix)
		for _ in ans:
			print(_ ,end = " ")
		print()

# } Driver Code Ends
