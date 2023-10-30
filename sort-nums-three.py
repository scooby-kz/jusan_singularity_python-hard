a,b,c = 1,3,2

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if c < b:
    c,b = b,c


print(a,b,c)