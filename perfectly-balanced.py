#massiv

def perfectly_balanced(arr):
    flag = False
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i-1:]):
            flag = True
    return flag


arr1 = [1, 2, 9, 8, 5, 7]
arr2 = [1, 2, 9, 8, 5, 7,5,1]

print(perfectly_balanced(arr1))
print(perfectly_balanced(arr2))