#User function template for Python

class Solution:
	def longestCommonSum(self, arr1, arr2, n): 
	    m={}
	    maxlen=0
	    s=0
	    temp=[0]*n
	    for i in range(n):
	        temp[i]=arr1[i]-arr2[i]
	    for i in range(n):
	        s=s+temp[i]
	        if s==0:
	            maxlen=max(maxlen,i+1)
	        if s in m:
	            maxlen=max(maxlen,i-m[s])
	        if s not in m:
	            m[s]=i
	    return maxlen
		# code here 

#{ 
#  Driver Code Starts
#Initial template for Python

def convertToBool(arr):
	a=[]
	for x in arr:
		if x == '1':
			a.append(True)
		else:
			a.append(False)
	return a

# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr1=input().strip().split()
        arr2=input().strip().split()
        arr1=convertToBool(arr1)
        arr2=convertToBool(arr2)
        ob = Solution()
        ans= ob.longestCommonSum(arr1, arr2, n)
        print(ans)
        tc=tc-1
# } Driver Code Ends
