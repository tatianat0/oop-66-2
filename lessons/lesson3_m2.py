"""3. Принципы ООП: Инкапсуляция, Абстракция. Гид- ветки"""
# class BankAccount:
#
#     def __init__(self, login, balance, password):
#         self.login = login
#         self._balance = balance
#         self.__password = password
#
# class VIPMember(BankAccount):
#
#     def __get_balance(self):
#         print(self._balance)
#
#     def test(self):
#         self.__get_balance()
#
#
# ardager = BankAccount("admin", 1000, "123")
# john = VIPMember("john", 1000, "123")
#
# # john.get_balance()
# # print(ardager.login)
# # print(ardager._balance)
# # print(dir(ardager))
#
#
from abc import ABC, abstractmethod
#
# #Абстрактный класс
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     @abstractmethod
#     def action(self):
#         pass
#
#
# class Dog(Animal):
#
#     def action(self):
#         print("Gaf Gaf")
#
#     def make_sound(self):
#         print("Step")
#
# class Duck(Animal):
#     def action(self):
#         print("Krya Krya ")
#
#     def make_sound(self):
#         print("Step")
#
#
# guffi = Dog()
# donald = Duck()

class SendOTP(ABC):
    @abstractmethod
    def send_otp(self):
        pass

class KGOtp(SendOTP):

    def send_otp(self):
        data = '''
            <Phone>+996779280699</Phone>
            <Text>Ваш код 1234</Text>
        '''
class RUOtp(SendOTP):

    def send_otp(self):
        data = {
            "Phone": "+79962101345",
            "Text": "Ваш код 1234"
        }