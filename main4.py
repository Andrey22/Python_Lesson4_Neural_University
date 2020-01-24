# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random);
import random
def choice_name(names, lenth):
    return random.choices(names, k=lenth)

listnames=['Kate', 'John', 'Nataly', 'Liza', 'John', 'Andrew', 'Olga', 'Mariana', 'Abraham', 'Julia', 'Ornella', 'Liza', 'Maria', 'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Samuil', 'Galina']

new_list = choice_name(listnames, lenth=100)

print(new_list)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
listcount=[]
for i in range(101):
    listcount=new_list.count('new_list[i]')
#     print(listcount)
# for i in range(101):
#     print (new_list(i))
# listcount=new_list.count("new_list")
# listsorted=list(sorted(listcount, reverse=True))

print(listcount)