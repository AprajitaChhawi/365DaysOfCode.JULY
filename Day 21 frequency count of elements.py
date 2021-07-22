class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        if N==0:
            return
        if N==1:
            arr[0]=1
            return
        m={}
        for i in arr:
            if i in m:
                m[i]=m[i]+1
            else:
                m[i]=1
        idx=0
        for i in range(1,N+1):
            if i in m:
                arr[idx]=m[i]
            else:
                arr[idx]=0
            idx=idx+1
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends
