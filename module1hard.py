def appropriation():
    alphabet_students = sorted(students)         #Сортировка оъектов списка в алфавитном порядке
    for i in range(0, len(students)):            #Цикл создает словарь из списка имен студ. (ключ) и ср. балов (значение)
        key = alphabet_students[i]
        value = sum(grades[i]) / len(grades[i])
        dict_students[key] = value
    print(dict_students)


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
dict_students = {}
appropriation()










