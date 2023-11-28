from math import gcd

def minimo_comun_multiplo(a,b):
    return a*b//gcd(a,b)

for _ in range(int(input())):
    r, v, a, n = map(int, input().split())

    r+=1
    v+=1
    a+=1
    
    ans = n//r + n//v + n//a 
    ans = ans - n//minimo_comun_multiplo(r,a) -n//minimo_comun_multiplo(r,v) -n//minimo_comun_multiplo(a,v) 
    ans += n//minimo_comun_multiplo(a,minimo_comun_multiplo(v,r))
    
    print(ans)