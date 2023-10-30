#Иницируем и Сортируем массив
arr = [1,2,3,4,5,6,7]
arr.sort()

# Находим середину
mediana = len(arr)//2
print('mediana',mediana)

#Условие
if len(arr)%2 == 0:
    print(arr[mediana-1])
else:
    print(arr[mediana])