grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students) #преобразование из множества в список
students_list.sort()     #упорядочил список в алфавитном порядке
a1 = float(sum(grades[0]) / len(grades[0]))  #присвоил значения для вычисления среднего
a2 = float(sum(grades[1]) / len(grades[1]))
a3 = float(sum(grades[2]) / len(grades[2]))
a4 = float(sum(grades[3]) / len(grades[3]))
a5 = float(sum(grades[4]) / len(grades[4]))
average_score = [a1, a2, a3, a4, a5] #список средних значений
zipped = zip(students_list, average_score) #соединение попарно
dict_ = dict(zipped) #создал словарь из обьединеных списков
print(dict_) #вывод результата