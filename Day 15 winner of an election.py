
#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        m={}
        for i in arr:
            if i in m:
                m[i]=m[i]+1
            else:
                m[i]=1
        a=0
        a1=""
        for index,values in sorted(m.items()):
            if int(m[index])>a:
                a=int(m[index])
                a1=index
        return a1,a
        # Your code here
        # return the name of the winning candidate and the votes he recieved


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends
