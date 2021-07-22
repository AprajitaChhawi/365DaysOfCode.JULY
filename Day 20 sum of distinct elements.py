#User function Template for python3
class Solution:
	
	def findSum(self,arr, n):
	    m={}
	    s=0
	    for i in arr:
	        if i in m:
	            m[i]=m[i]+1
	        else:
	            m[i]=1
	            s=s+i
	    return s
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
