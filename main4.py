import random
from random import choices
# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random);
# def choisename(list3, N):
# # for i in range(N):
#     index=random.randint(N)
#     list.append(list2,list1(index))
#     return list2
#
# list3=['Alex','Ivan', 'Sveta', 'Sima']
# print (list3)
#
# # list2=choisename(['Alex','Ivan', 'Sveta', 'Sima'],8)
#
# N=8
# list2=choisename(list3, N)
#
# print (list2)
#
# from random import choices



def choice_name(names, len_list):

    return 1


list1=['Kate', 'Adam', 'Nataly', 'Lisa', 'John', 'Kate', 'Olga', 'Maria', 'Artem', 'Julia', 'Olga', 'Lisa', 'Maria', 'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Sam', 'Garry']
my_list = choice_name(list1, len_list=100)

print(my_list)