"""Урок №5 Декораторы venv"""
# Декораторы — это функции, которые принимают другую функцию и расширяют её поведение, не изменяя её код.

#
# def simple_decorator(func):
#     def wrapper():
#         print("До выполнения!!")
#         func()
#         print("после выполнения!!")
#     return wrapper
#
# @simple_decorator
# def say_hello():
#     print("Hello!!")
#
# # say_hello()
#
# # 3
# def greeting_decorator(func):
#     # 4
#     def wrapper(name):
#         print(f"{name} Привет!!") # 5
#         func(name) # 6
#     return wrapper # 7
#
# @greeting_decorator #2
# def greet(name):
#     print(f"{name} как дела ?")
#
# # greet("Ardager") #1
#
# # @greeting_decorator
# # def tttt(arg):
#
# def repeat_decorator(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator
#
# @repeat_decorator(5)
# def hi():
#     print('HI!!')
# # hi()
#
# def class_decorator(cls):
#     class NewClass(cls):
#         def action1(self):
#             print("New action!!")
#     return NewClass
#
# # @class_decorator
# class OldClass:
#     def action(self):
#         print('Old action!!')
# test_obj = OldClass()
# # test_obj.action()
# # test_obj.action1()
# print(type(test_obj))
#
# # def is_admin():
# #     pass
# #
# # @is_admin
# # def ban_user(user):
# #     user.is_activa = False

""" Шаг 1 — Сначала пойми: функции в Python это объекты
# В Python функцию можно передать в другую функцию, как обычную переменную: """

def say_hello():
    print("Привет!")
def run(func):            # принимаем функцию как аргумент
    func()                # и вызываем её

# run(say_hello)            # Привет!  # передаём функцию БЕЗ скобок

""" Шаг 2 — Функция внутри функции
В Python можно создать функцию внутри другой функции: """

def outer():
    print("Я снаружи")

    def inner():
        print("Я внутри")

    inner()              # вызываем внутреннюю, без неё "Я внутри" не выйдет
# outer()                  # Я снаружи
                         # Я внутри
""" Шаг 3 — Теперь собираем декоратор. Декоратор — это функция, которая:
1. Принимает функцию
2. Создаёт новую функцию-обёртку внутри себя
3. Возвращает эту обёртку """

def my_decorator(func):           # 1. принимаем функцию
    def wrapper():                # 2. создаём обёртку
        print("До вызова")
        func()                    # вызываем оригинальную
        print("После вызова")
    return wrapper                # 3. возвращаем обёртку

""""""" Используем без @: """""""
def say_hello():
    print("Привет!")

say_hello = my_decorator(say_hello)  # оборачиваем вручную
say_hello()                          # До вызова
                                     # Привет!
                                     # После вызова

""""" Используем с @ — это просто короткая запись того же самого:"""""
@my_decorator
def say_hello():
    print("Salut!")
say_hello()

# @my_decorator = say_hello = my_decorator(say_hello) — это одно и то же!

""" Шаг 4 — А если функция принимает аргументы?
Что если твоя функция принимает какие-то данные?"""

def say_hello(name):                  # ← принимает аргумент
    print(f'Привет, {name}')
say_hello('Татьяна')                  # ← передаём аргумент

# Проблема — обёртка wrapper() не принимает аргументы и упадёт с ошибкой.
# Решение — использовать *args, **kwargs, что означает "прими любые аргументы и передай дальше":

def m_decorator(func):
    def wrapper(*args, **kwargs):    # ← принимаем любые аргументы
        print('До вызова')
        func(*args, **kwargs)        # ← передаём их дальше
        print('После вызова')
    return wrapper

# Теперь декоратор работает с любой функцией.
@m_decorator
def say_hello(name):
    print(f'Привет, {name}')
say_hello('Алина')

""" Шаг 5 — Реальный пример: замер времени"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()           # запомнили время ДО
        result = func(*args, **kwargs)
        end = time.time()             # запомнили время ПОСЛЕ
        print(f"Выполнялось: {end - start:.2f} сек")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Готово!")

slow_function()

""" Итого — вся логика на одной схеме

@my_decorator
def say_hello():        ← твоя оригинальная функция
    print("Привет!")

         ↓ Python делает это автоматически

say_hello = my_decorator(say_hello)

         ↓ когда вызываешь say_hello()

wrapper()               ← вызывается обёртка
  → print("До")
  → func()              ← внутри вызывается оригинал
  → print("После") """
