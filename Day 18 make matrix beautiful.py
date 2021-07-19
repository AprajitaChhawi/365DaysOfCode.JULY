
#User function Template for python3

class Solution:
    
    #Function to find minimum number of operations that are required 
    #to make the matrix beautiful.
    def findMinOpeartion(self, matrix, n):
        l=[]
        s=0
        for i in range(n):
            row=0
            col=0
            for j in range(n):
                row=row+matrix[i][j]
                col=col+matrix[j][i]
                s=s+matrix[i][j]
            l.append(row)
            l.append(col)
        return max(l)*n-s        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        print(obj.findMinOpeartion(matrix,n))



# } Driver Code Ends
