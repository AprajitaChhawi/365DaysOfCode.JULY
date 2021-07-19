#User function Template for python3

class Solution:
    def maxWater(self, arr, n):
        l=[0]*n
        r=[0]*n
        l[0]=arr[0]
        r[-1]=arr[-1]
        for i in range(1,n):
            l[i]=max(l[i-1],arr[i])
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],arr[i])
        s=0
        for i in range(n):
            s=s+min(l[i],r[i])-arr[i]
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
        ans = ob.maxWater(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
