"""Урок №2 Принципы ООП -  Наследование, Полиморфизм."""

# Родительский|Супер класс
class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        print(f"{self.name} base action")


# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, hp, lvl, mp):
        super().__init__(name, hp, lvl)
        self.mp = mp

    def cast_spell(self):
        print('Огненный щар!!')

    def action(self):
        print(f"Это новый метод дочернего класса!! {self.name}")


kirito = Hero("KIrito", 100, 10)
asuna = MageHero("Asuna", 1000, 100, 100)

# kirito.action()
# asuna.action()

class Fly:
    def action(self):
        print("Fly")

class Swim:
    def action(self):
        print("Swim")

class Animal(Fly, Swim):
    # def action(self):
    #     print("Step")
    pass

donald_duck = Animal()

# donald_duck.action()




class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print('B')
class C(A):
    def action(self):
        super().action()
        print('C')
class D(C, B):
    def action(self):
        super().action()
        print('D')

test_obj = D()

print(D.__mro__)