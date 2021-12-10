#!/usr/bin/env python
# coding: utf-8

# # Декораторы
#
# В этом домашнем задании мы напишем собственные дектораторы, которые будут менять системные объекты. Но для начала мы с вами познакомимся с функцией `write`.

# In[20]:


import sys

sys.stdout.write('Hello, my friend!')

# Это метод объектов file-like классов, то есть классов, которые реализуют семантику "Меня можно создать, из меня можно прочитать и в меня можно записать".
#
# Самый главный пример такого объекта -- объект `file`, являющийся результатом вызова фукнции `open()`. Для простоты и универсальности взаимодействия, стандартный ввод и стандартный вывод тоже являются файлами, из которых можно читать и в которые можно писать.

# In[21]:


output = open("./some_test_data.txt", 'w')

# In[22]:


output.write('123')

# In[23]:


output.close()

# Как вы могли заметить, функция возвращает число записанных байт. Это важная часть контракта, которую нужно поддержать, если вы хотите как-то подменять эту функцию.

# ## Задача 1

# Для начала, давайте подменим метод `write` у объекта `sys.stdin` на такую функцию, которая перед каждым вызовом оригинальной функции записи данных в `stdout` допечатывает к тексту текущую метку времени.

# In[24]:

from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    original_write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: {string_text}")


sys.stdout.write = my_write

# In[25]:


print('1, 2, 3')

# In[26]:


sys.stdout.write = original_write


# Вывод должен был бы быть примерно таким:

# ```
# [2021-12-05 12:00:00]: 1, 2, 3
# ```

# ## Задача 2
#
# Упакуйте только что написанный код в декторатор. Весь вывод фукнции должен быть помечен временными метками так, как видно выше.

# In[8]:


def timed_output(function):
    def wrapper(name: str, *args, **kwargs):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: ", end='')
        function(name)

    return wrapper


# In[9]:


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


# In[10]:


print_greeting("Nikita")


# Вывод должен быть похож на следующий:
#
# ```
# [2021-12-05 12:00:00]: Hello, Nikita!
# ```

# ## Задача 3
#
# Напишите декторатор, который будет перенаправлять вывод фукнции в файл.
#
# Подсказка: вы можете заменить объект sys.stdout каким-нибудь другим объектом.

# In[27]:


def redirect_output(filepath):
    def decorator(func):
        sys.stdout = open(filepath, 'w')

        def wrapper(*args, **kwargs):
            return func()

        return wrapper

    return decorator


# In[28]:


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


# In[29]:


calculate()

# In[30]:


get_ipython().run_line_magic('cat', 'function_output.txt')

# In[ ]:
