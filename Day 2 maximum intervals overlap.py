#User function Template for python3

class Solution:

    def findMaxGuests(self, Entry, Exit, N):
        Entry.sort()
        Exit.sort()
        i=1
        j=0
        res=1
        count=1
        max_count=1
        ent=Entry[0]
        while(i<N and j<N):
            if Entry[i]<=Exit[j]:
                count=count+1
                if count>max_count:
                    max_count=count
                    ent=Entry[i]
                i=i+1
            else:
                j=j+1
                count=count-1
        return max_count,ent
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        
        N = int(input())

        entry = [int(x) for x in input().split()]
        exit =  [int(x) for x in input().split()]

        solObj = Solution()
        ans = solObj.findMaxGuests(entry, exit, N) 
        print(ans[0],ans[1])
        

# } Driver Code Ends
