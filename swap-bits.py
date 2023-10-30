num = 15
res = '0000'
while num > 0:
    res += str(num%2)
    num = num//2
print(res)


nums_list = list(res)

# если число больше или меньше 8 битов
if len(nums_list) > 8:
    while len(nums_list) != 8:
        nums_list.pop(0)
else:
    while len(nums_list) != 8:
        nums_list.insert(0,0)

nums_list = list(reversed(nums_list))
print(nums_list)
final = 0


for i,k in (zip(range(7,0,-1), nums_list)):
    final += (2**int(i)*int(k))
    print(final)
    
print(final)