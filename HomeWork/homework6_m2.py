"""Часть 1 — Внешние зависимости"""
# Эта библиотека нужна для отправки запросов в интернет.
# С помощью requests можно получать данные с сайтов и API.
import requests

response = requests.get("https://api.github.com")
print("Статус ответа:", response.status_code)
print("Тип контента:", response.headers["content-type"])



# Эта библиотека нужна для генерации случайных фейковых данных.
# Faker создаёт имена, адреса, телефоны и другие данные для тестирования.
from faker import Faker

fake = Faker("ru_RU")
print("Имя:", fake.name())
print("Адрес:", fake.address())
print("Телефон:", fake.phone_number())
print("Email:", fake.email())
print("Компания:", fake.company())



# Эта библиотека нужна для изменения цвета текста в терминале
from colorama import init, Fore
init()
print(Fore.RED + "Этот текст красный")
print(Fore.GREEN + "Этот текст зелёный")
print(Fore.BLUE + "Этот текст синий")
print(Fore.RESET + "А этот текст обычный")



# Эта библиотека нужна для генерации случайных чисел и случайного выбора.
# Random2 — это улучшенная версия стандартного модуля random.
import random2

print("Случайное число:", random2.randint(1, 100))

fruits = ["яблоко", "банан", "апельсин", "манго", "киви"]
print("Случайный фрукт:", random2.choice(fruits))

random2.shuffle(fruits)
print("Перемешанный список:", fruits)


"""Часть 2 — Алгоритм (LeetCode)"""

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])