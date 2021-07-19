#User function Template for python3
class Solution:
	def matSearch(self,mat, N, M, X):
	    top=0
	    right=M-1
	    while(top<N and right>=0):
	        if mat[top][right]==X:
	            return 1
	        elif mat[top][right]>X:
	            right=right-1
	        else:
	            top=top+1
	    return 0
		# Complete this function

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends
