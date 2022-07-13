# 1. Вывести из строки подмножество без повторений символов максимальной длины. 
"""
Пример работы алгоритма:
* входное значение: 'ffgabnnkmm'
* ответ: fgabn 
"""

def without_repeating_characters(String1):
  l = []
  for i in String1:
    if not i in l:
      l.append(i)
  return l

S = 'ffgabnnkmm'
S = 'ffgabnndzasdfghjkllkjhgfdsasfghjksl;'
print(*without_repeating_characters(S))


#2. Проверить, упорядочены ли элементы в списке по возрастанию
"""
Пример работы алгоритма:
* входное значение: [5,3,7]
* ответ: нет
* входное значение: [5,6,7]
* ответ: да
"""
def сheck_ascending(lst):
  tmp = sorted(lst)
  return tmp == lst

List = [5, 3, 7]
print(сheck_ascending(List))

List = [5, 6, 7]
print(сheck_ascending(List))


#3. Вывести 3 максимальных значения из списка в порядке убывания
"""
Пример работы алгоритма:
* входное значение: [1, 9, 6, 4, 2, 7, 5]
* ответ: [9, 7, 6]
"""
def max_3_numbers(lst):
  max_1 = max(lst)
  lst.remove(max_1)
  max_2 = max(lst)
  lst.remove(max_2)
  max_3 = max(lst)
  return max_1, max_2, max_3

List = [1, 9, 6, 4, 2, 7, 5]
print(max_3_numbers(List))


#4. Подсчитать количество четных и нечетных элементов списка
"""
Пример работы алгоритма:
* входное значение: [1, 9, 6, 4, 2, 7, 5]
* ответ: [3, 4]
"""

def number_of_even_and_odd(lst):
  number_even = len([i for i in lst if i % 2 == 0])
  number_oven = len(lst) - number_even
  return number_even, number_oven

List = [1, 9, 6, 4, 2, 7, 5]
print(number_of_even_and_odd(List))

#5. Создать массив случайных чисел. Найти значение, которое повторяется в массиве чаще всего.
import numpy as np

def most_frequent_value(array):
  return np.bincount(x).argmax()

x = np.random.randint(2, 10, size = 7)
print(x)

print(most_frequent_value(x))


#6. Создать массив единиц размера 9х9. Заменить нулем элементы массива, имеющие четный индекс

import numpy as np

def replace_with_0(arr):
  for i in range(9):
    for j in range(9):
      if i % 2 == 1 and j % 2 == 1:
        arr[i][j] = 0
  return arr

x = np.random.randint(1, 2, size =(9, 9))
print(x)
print('- - - - - - - - - - - -')
print(replace_with_0(x))

#7. Создать массив случайных чисел. Для некоторого случайного значения 𝑛 найти ближайшее значение в массиве.
import numpy as np
def func_2(arr, n):
  l = [i for i in arr if n >= i]
  if len(l) == 0:
    return min(arr)
  else:
    return max(l)

N = 4
array = np.random.randint(0, 10, size=10)
print(array)
print(func_2(array, N))

#8. Создать массив случайных чисел. Произвести подсчет повторений всех элементов в массиве
import numpy as np

def func(arr):
    l = []
    for i in range(len(arr)):
        tmp = 1
        j = i + 1
        if arr[i] in l:
            continue
        while j < len(arr):
            if arr[i] == arr[j] and i <= j:
                tmp = tmp + 1
                l.append(arr[i])
            j = j + 1
        print(arr[i], "->", tmp)

x = np.random.randint(2, 10, size=30)
print(x)
func(x)


#5. Создать массив случайных чисел. Каждый четный элемент массива заменить значением 0
import numpy as np
def zero(num):
  for i in range(len(num)):
    if num[i] % 2 == 0:
      num[i] = 0
  return num

x = np.random.randint(2, 10, size = 7)
print(x)

print(zero(x))


#1. Для каждого значения в столбце A вывести первые 3 строки, упорядоченные по C
import pandas as pd
import numpy as np

def df_func(data):
    dt_gr = data.groupby('A')
    for i in dt_gr:
        print(i[1].sort_values(by=['C']).head(3))
    

df = pd.DataFrame()
df['A'] = np.random.randint(0, 10, 30)
df['B'] = np.random.randint(0, 100, 30)
df['C'] = np.random.randint(0, 100, 30)

df_func(df)

###2. Для каждого значения в столбце А найти сумму всех значений столбца B

import numpy as np
import pandas as pd

def df_func(df):
  print(df.groupby('A').agg({'C':sum}))
    

df = pd.DataFrame()
df['A'] = np.random.randint(0, 10, 30)
df['B'] = np.random.randint(0, 100, 30)
df['C'] = np.random.randint(0, 100, 30)

print(df)
print('- - - - - - -')
df_func(df)