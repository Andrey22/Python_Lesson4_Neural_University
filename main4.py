# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе
# список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random);
import random
def choice_name(names, length):
    return random.choices(names, k=length)

listnames=['Kate', 'John', 'Nataly', 'Liza', 'John', 'Andrew', 'Olga', 'Mariana', 'Abraham', 'Julia', 'Ornella', 'Liza', 'Maria', 'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Samuil', 'Galina']

new_list = choice_name(listnames, length=100)

print(new_list)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
def frequentname(listname):
    dict = {}
    for name in listname:
        dict[name] = dict.get(name,0) + 1
    dict = list(dict.items())
    dict.sort(key=lambda x: x[1], reverse=True)
    # x[1]  означает сортировку по Values, т.е. по количеству повторений имени в словаре (имя, количество повторений)
    return dict[0][0]

print(frequentname(new_list))

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.

def rareletter(list2):
    dict2 = {}
    for name in list2:
        for char in name:
            dict2[char] = dict2.get(char,0) + 1
    dict2 = list(dict2.items())
    dict2.sort(key=lambda x: x[1])
    # x[1]  означает сортировку по Values, т.е. по количеству повторений имени в словаре (имя, количество повторений)
    return dict2[0][0]
print(rareletter(new_list))

