a, b, c = map(int, input().split())
if a >= b >= c or a <= b <= c:
    print(b)
elif b >= a >= c or b <= a <= c:
    print(a)
else:
    print(c)
