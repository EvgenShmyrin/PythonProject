# #################################################strings ##########################################
# 1) написати прогу, яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# 2,3,5,4,4        #вивело в консолі.
#
# st = 'as 23 fdfdg544'  # введена строка
# for i in st:
#     if i.isdigit():
#         print(i, end=",")

# 2)написати прогу, яка вибирає зі введеної строки числа і виводить їх так, як вони написані
# наприклад:
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'  # введена строка
#
# print(', '.join(''.join(num if num.isdigit() else ' ' for num in st).split()))

####################################################list comprehension#######################################
# 1) є строка: greeting = ‘Hello, world’
# записати кожний символ, як окремий елемент списку, і зробити його заглавним:
# [‘H’, ‘E’, ‘L’, ‘L’, ‘O’, ‘,’, ‘ ‘, ‘W’, ‘O’, ‘R’, ‘L’, ‘D’]
# greeting = 'Hello, world'
# li = []
# for letter in greeting:
#     li.append(letter.upper())
# print(li)

# 2) з діапазону від 0-50 записати тільки непарні числа, при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, …]
#
# print([num ** 2 for num in range(0, 50) if num % 2 != 0])

###################################################function##########################################
# – створити функцію, яка виводить List
#
# li = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# def func():
#     print(list(li))
# func()
#
# – створити функцію, яка приймає три числа, та виводить та повертає найбільше.
#
# def maxFun(a, b, c):
#     b = max(a, b, c)
#     print(b)
#     return b
# maxFun(1,2,3)
#
# – створити функцію, яка приймає будь-яку кількість чисел, повертає найменше, а виводить найбільше
#
# def max_func(*args):
#     print(max(args))
#     b = min(args)
#     return b
# max_func(1,2,3,4,5, 86, 3, 6)
#
# – створити функцію, яка повертає найбільше число з List
#
# list_ = [34, 5, 343, 34, 68, 98, 2, 49]
# def max_fun_list(list_):
#     max_value = max(list_)
#     return max_value
#
# – створити функцію, яка повертає найменше число з List
#
# list_ = [34, 5, 343, 34, 68, 98, 2, 49]
# def min_fun_list(list_):
#     min_value = min(list_)
#     return min_value
# print((min_fun_list(list_)))
#
# – створити функцію, яка приймає List чисел та складає значення елементів List та повертає його.
#
# def summ_fun(num):
#     return sum(num)
# print(summ_fun([34,5,67,9,1]))
# #
# – створити функцію, яка приймає List чисел та повертає середнє арифметичне його значень.
#
# def avr_fun(num):
#     return sum(num)/len(num)
# print(avr_fun([23,45,6,7,2,89]))
#
# 1 Є list:
# – знайти  мін. число

list_my = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

def min_number():
    print(min(list_my))

# – видалити усі дублікати
def delete_duplicate():
    set_list = set(list_my)
    new_list = list(set_list)
    print(new_list)

# – замінити кожне 4-те значення на ‘X’
def copy_list():
    print(['X' if (key + 1) % 4 == 0 else valume for key, valume in enumerate(list_my)])

# 2) вивести на екран пустий квадрат з “*”, сторона якого вказана як аргумент функції

def square(num):
    for i in range(num):
        if i == 0 or i == num - 1:
            print('*' * num)
        else:
            print('*' + ' ' *(num-2) + '*')

# 3) вивести табличку множення за допомогою циклу while

def table():
    i=1
    while i < 10:
        j = 1
        while j < 10:
            rez = f'{i}*{j}={i*j}'
            print(f'{rez:8}', end='')
            j += 1
        i += 1
        print('')

# 4) переробити це завдання під меню
print('1) Знайти  мін. число.')
print('2) Видалити усі дублікати.')
print('3) Замінити кожне 4-те значення на ‘X’.')
print('4) Вивести на екран пустий квадрат з “*”, сторона якого вказана як аргумент функції.')
print('5) Вивести табличку множення за допомогою циклу while.')
print('9) Вихід.')
print('')
set = input('Зробіть свій вибір')

if set == '1':
    min_number()
elif set == '2':
    delete_duplicate()
elif set == '3':
    copy_list()
elif set == '4':
    square(10)
elif set == '5':
    table()
elif set == '9':
    break


