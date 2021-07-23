#User function Template for python3

class Solution:
    def countBits(self, N, A):
        ans=0
        res=0
        for i in range(0,32):
            count=0
            for j in range(N):
                if(A[j]&(1<<i)):
                    count=count+1
            res=max(res,count)
        return max(res,count)
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for it in range(N):
            A[it] = int(A[it])
        
        ob = Solution()
        print(ob.countBits(N, A))
# } Driver Code Ends
