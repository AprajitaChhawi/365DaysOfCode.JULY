#User function Template for python3

class Solution:
    def distinct(self, M, N):
        m={}
        count=0
        for i in range(N):
            a=list(set(M[i]))
            for j in range(0,len(a)):
                if a[j] not in m:
                    m[a[j]]=1
                else:
                    m[a[j]]=m[a[j]]+1
        for i,j in m.items():
            if j==N:
                count=count+1
        return count
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        M = [[0]*N for i in range(N)]
        for itr in range(N*N):
            M[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.distinct(M, N))
# } Driver Code Ends
