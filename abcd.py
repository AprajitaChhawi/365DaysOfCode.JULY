class Solution:
    def sortByFreq(self,a,n):
        l=[]
        m={}
        for i in a:
            if i in m:
                m[i]=m[i]+1
            else:
                m[i]=1
        k=dict(sorted(m.items(),key=lambda x:x[0]))
        l1=dict(sorted(k.items(),key=lambda x:x[1],reverse=True))
        print(k)
        for idx,value in l1.items():
            while(value):
                l.append(idx)
                value=value-1
        return l
        


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(a,n)
        print(*l)
