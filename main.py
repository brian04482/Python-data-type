# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# def main_func(func1):
#     print('after main')
#     def wrapper():
#         print('wrapper')
#         func1()
#         print('the end!')
#     return wrapper
# @main_func
#
# def func_test():
#     print('i from func')

n: int = 10
n = 10.123
# print(n)
# print(type(n))
# n = int(n)
# print(type(n))
# print(n)
# text = 'Hello "world"'
# print(text)

# если нужно обратиться к какому-то по счету символу, начиная с конца, то можно указывать отрицательные значения (на этот раз с единицы).
# string1 = 'interface FastEthernet1/0'
# print(string1[1])
# print(string1[-2])

# Кроме обращения к конкретному символу, можно делать срезы строк, указав диапазон номеров (срез выполняется по второе число, не включая его):

# print(string1[0:9])
# print(string1[10:22])
#
# # Если не указывается второе число, то срез будет до конца строки:
# print(string1[10:])

# также в срезе можно указывать шаг. Так можно получить нечетные числа:

# string2 = '0123456789'
# print(string2[1::2])

# # А таким образом можно получить все четные числа строки
# print(string2[0::2])
# # или
# print(string2[::2])


# Срезать три последних символа строки:

# print(string2[-3:])

# Срезы также можно использовать для получения строки в обратном порядке:

# print(string2[::])
# print(string2[:-4])
#
# # или же берем каждый 4 элемент с конца начиная с первого с конца
# print(string2[::-4])

# Функция len позволяет получить количество символов в строке:

# string3 = 'interface Gi0/1'
# print(len(string3))

# Создание списка с помощью функции list():
# list1 = list('router')
# print(list1)

# Так как список - это упорядоченный тип данных, то, как и в строках, в списках можно обращаться к элементу по номеру, делать срезы:
# list2 = [1, 20, 4.0, 'word']
# print(list2[1])
# print(list2[1::])
# print(list2[-1])
# print(list2[::-1])

# # Перевернуть список наоборот можно и с помощью метода reverse():
# vlans = ['10', '15', '20', '30', '100-200']
# vlans.reverse()
# print(vlans)

# Так как список - это упорядоченный тип данных, то, как и в строках, в списках можно обращаться к элементу по номеру, делать срезы:

# list2 = [1, 20, 4.0, 'word']
# print(list2[1])
# print(list2[1::])
# print(list2[-1])
# print(list2[::-1])

# # Перевернуть список наоборот можно и с помощью метода reverse():
# vlans = ['10', '15', '20', '30', '100-200']
# vlans.reverse()
# print(vlans)

# Так как списки изменяемые, элементы списка можно менять:
# list2 = [1, 20, 4.0, 'word']
# list2[0] = 'test'
# print(list2)

# функция sorted сортирует элементы списка по возрастанию и возвращает новый список с отсортированными элементами:
# names = ['John', 'Michael', 'Antony']
# print(sorted(names))


# # Создать пустой кортеж:
# tuple1 = tuple()
# print(tuple1)
# ()
#
# # Кортеж из одного элемента (обратите внимание на запятую):
# tuple2 = ('password',)
# print(tuple2)
# # Кортеж из списка:
#
# list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
# tuple_keys = tuple(list_keys)
# # print(tuple_keys)

# К объектам в кортеже можно обращаться, как и к объектам списка, по порядковому номеру:

# print(tuple_keys[0])

# Но так как кортеж неизменяем, присвоить новое значение нельзя:

# tuple_keys[1] = 'test'

# Но! есть вариант, добавить кортеж к кортежу
# t = ('mac',)
# print(id(tuple_keys))
# tuple_keys += t
# print(tuple_keys)
# print(id(tuple_keys))
#
# print(tuple_keys.)

# Функция sorted сортирует элементы кортежа по возрастанию и возвращает новый список с отсортированными элементами:

# print(sorted(tuple_keys))
# t = 5
# print(id(t))
# t =+ 1
# print(id(t))
# lst = [1 ,2 ,4 ,5]
# print(id(lst))
# lst.append(6)
# print(lst)
# print(id(lst))

# С помощью множества можно легко убрать повторяющиеся элементы:

# vlans = [10, 20, 30, 40, 100, 10]
#
# set(vlans)
# set1 = set(vlans)
# print(set1)

# # Нельзя создать пустое множество с помощью литерала (так как в таком случае это будет не множество, а словарь):
# set1 = {}
# print(type(set1))
#
# # Но пустое множество можно создать таким образом:
#
# set2 = set()
# print(type(set2))
#
# # Множество из строки:
#
# set3 = set('long long long long string')
# print(set3)

# Множество из списка:

# set4 = set([10, 20, 30, 10, 10, 30])
# print(set4)

# Или же по другому, фильтруем список от повторяющихся элементов
# s = [1, 1, 1, 1,]
# s = list(set(s))
# print(type(s))
# print(s)


# Для того, чтобы получить значение из словаря, надо обратиться по ключу, таким же образом,
# как это было в списках, только вместо номера будет использоваться ключ:

# london = {'name': 'London1', 'location': 'London Str'}
# print(london['name'])
# print(london['location'])
#
# # Аналогичным образом можно добавить новую пару ключ-значение:
#
# london['vendor'] = 'Cisco'
# print(london)
#
# # В словаре в качестве значения можно использовать словарь:
#
# london_co = {
#     'r1': {
#         'hostname': 'london_r1',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.1'
#     },
#     'r2': {
#         'hostname': 'london_r2',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.2'
#     },
#     'sw1': {
#         'hostname': 'london_sw1',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '3850',
#         'ios': '3.6.XE',
#         'ip': '10.255.0.101'
#     }
# }
# # Получить значения из вложенного словаря можно так:

# print(london_co['r1']['ios'])
# print(london_co['r1']['model'])
# print(london_co['sw1']['ip'])
#
# # Функция sorted сортирует ключи словаря по возрастанию и возвращает новый список с отсортированными ключами:
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(sorted(london))
d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
r1 = dict.fromkeys(d_keys)
print(r1)
