#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        m={}
        for i in arr:
            if i in m:
                m[i]=m[i]+1
            else:
                m[i]=1
        for i in range(n):
            if m[arr[i]]>1:
                return i+1
        return -1
        
        #arr : given array
        #n : size of the array

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends
