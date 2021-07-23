
#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        for i in range(n):
            if arr[i]==0:
                arr[i]=-1
        m={}
        c=0
        s=0
        for i in range(n):
            s=s+arr[i]
            if s==0:
                c=c+1
            if s in m:
                c=c+m[s]
            if s not in m:
                m[s]=1
            else:
                m[s]=m[s]+1
        return c
        #Your code here
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
