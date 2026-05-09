# Домашнее задание № 2
from HomeWork.homework1_m2 import Hero


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        return f'{self.name} - Воин атакует мечом!'

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        return f'{self.name} - Маг кастует заклинание!'

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        return f'{self.name} - Ассасин атакует из - под тишка!'


din = Warrior("Дин", 2, 8, 90, 30)
kass = Mage("Касс", 3, 5, 100, 25)
lilit = Assassin("Лилит", 1, 3, 80, 20)

print(din.greet())
print(din.attack())
print(din.rest(1))

print(kass.greet())
print(kass.attack())
print(kass.rest(2))

print(lilit.greet())
print(lilit.attack())
print(lilit.rest(2))

# Мини-игра "Камень, Ножницы, Бумага"
