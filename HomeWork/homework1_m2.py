# Домашнее задание №1 Тема: Создание класса в Python
# Задание: Вам необходимо создать класс Hero со следующими характеристиками:
# Атрибуты класса:
# name — имя героя
# level — уровень героя
# health — здоровье героя
# strength — сила героя

# Методы класса:
# 1)greet()
# Метод должен выводить сообщение: Привет, я {имя героя}, мой уровень {уровень}
# 2) attack()
# Метод должен: выводить сообщение: {имя героя} наносит удар! уменьшать силу героя на 1
# 3) rest()
# Метод должен: выводить сообщение: {имя героя} отдыхает… увеличивать здоровье героя на 1
#
# Дополнительное требование:
# Создать минимум 2 объекта класса Hero. Вызвать у каждого объекта все созданные методы.
# Проверить, что параметры действительно изменяются.
# 📦 Что нужно сдать Файл.py с выполненным заданием Залить код в свой
# GitHub репозиторий Прикрепить ссылку на репозиторий

class Hero:
     def __init__(self, name, level, health, strength):
         self.name = name
         self.level = level
         self.health = health
         self.strength = strength

     def greet(self):
         return f'Привет, Я {self.name}, мой уровень {self.level} '

     def attack(self, amount):
         self.strength -= amount
         return f'{self.name}, наносит удар! Сила: {self.strength}'

     def rest(self, amount):
         self.health += amount
         return f'{self.name} отдыхает... Здоровье: {self.health}'



mario = Hero("Mario", 1, 10, 100)
sora = Hero("Sora", 2, 5, 80)


print(mario.greet())
print(mario.attack(1))
print(mario.rest(1))

print(sora.greet())
print(sora.attack(1))
print(sora.rest(1))


