
#User function Template for python3

class Solution:
    
    #Function to exchange first column of a matrix with its last column.
    def exchangeColumns(self,matrix):
        r=len(matrix)
        c=len(matrix[0])
        top=0
        bottom=r-1
        right=c-1
        while(top<=bottom):
            matrix[top][0],matrix[top][right]=matrix[top][right],matrix[top][0]
            top=top+1
        return matrix  
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        obj.exchangeColumns(matrix)
        
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
        print()
        
# } Driver Code Ends
