def pgcd(n,m):
    r=n%m
    while(r>0):
        d=r
        r=m%r
        m=d
    return(m)
print(pgcd(128,8))
        