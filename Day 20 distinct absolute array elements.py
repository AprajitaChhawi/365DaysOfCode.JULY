

class Solution:
    def distinctCount(self, arr, n):
        m={}
        count=0
        for i in arr:
            temp=abs(i)
            if temp in m:
                m[temp]=m[temp]+1
            else:
                m[temp]=1
        for j in m.values():
            count=count+1
        return count
        # code here

#{ 
#  Driver Code Starts





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.distinctCount(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
