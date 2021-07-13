
class Solution:
	def overlappedInterval(self, Intervals):
	    n=len(Intervals)
	    Intervals.sort(key=lambda x:x[0])
	    m=[]
	    res=0
	    for i in range(1,n):
	        if Intervals[res][1]>=Intervals[i][0]:
	            Intervals[res][1]=max(Intervals[res][1],Intervals[i][1])
	            Intervals[res][0]=min(Intervals[res][0],Intervals[i][0])
	        else:
	            res=res+1
	            Intervals[res]=Intervals[i]
	    for i in range(res+1):
	        m.append(Intervals[i])
        return m
		#Code here

#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends
