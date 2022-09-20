def add_fractions(a,b,c,d):
    if b==d:
        chislit=a+c
        znamenat=b
    else:
        chislit = a*d + c*b
        znamenat = b*d
    k=0
    for i in range(1, chislit+1):
        if znamenat % i==0 and chislit % i==0:
            k=max(i,k)
    return int(chislit / k), int(znamenat / k)

print(add_fractions(int(input()),int(input()),int(input()),int(input())))
