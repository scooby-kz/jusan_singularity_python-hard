#Тестовые данные
arr1 = [1, 1, 3, 2, 5]
arr2 = [1, 3, 9, 1, 5, 7]
#результирущий список
res = []

#если число из арр2 нету в арр1 добавляем в результат
for i in arr2:
    if i not in arr1:
        res.append(i)

#Сортируем и выводим
print(sorted(res))