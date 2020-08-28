def coinchangedp(n,coins):
    l=list()
    l.append(0)
    for i in range(1,n+1):
        m=n+1
        for j in coins:
            z=i-j
            if z>=0:
                new=l[z]+1
                res=min(new,m)
                m=res
        l.append(m)
    return l[n]


n=int(input())
coins=[1,3,4]
print(coinchangedp(n,coins))


        
