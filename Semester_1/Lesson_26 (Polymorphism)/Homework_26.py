"""
1. Создать класс с атрибутами: name, email, password, purchases (список), card 
методами: 
- purchase - метод для покупки товаров. 
- register - создать нового пользователя и включить его в список пользователей. 
    name - должен содержать только буквы 
    email - должен содержать @ 
    password - миинмальная длинна 6 
    card - длина ключа code была равна 16 
- login - вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные:  
    покупки, список игр и т.д 
- add_product - добавить куплейнный товар в атрибут purchases

PRUDUCTCS = {
    "Telephone": 25,
    "Computer": 150,
}

USERS = [
    {
        "name": "Oybek",
        "password": "123456",
        "email": "mail@gmail.com",
        "purchases": [],
        "card": {"code": "1234567890123456", "money": 1000}
    }
]

class Store:
    pass

person_1 = Store()
"""

class Store:
    def __init__(self, name, email, password, card):
        self.name = name 
        self.email = email
        self.password = password 
        self.card = card
    
class Person_1(Store):
    def __init__(self, name, email, password, card, purchases):
        self.purchases=[]

    def name (self, name):
        name = (input('Введите имя: '))
        name.isalpha()
        if name.isalpha == False:
            print('ты ввёл неверное имя')

    def email (self, email):
        email = (input('Введите email: '))
        if "@" not in email:
            print('ты ввёл неправельный адрес email')

    def password (self, card):
        password = (input('Введите пароль: '))
        if len(card) <=5:
            print('пароль должен содержать 6 или более символов')

    def card (self, card):
        card = (input('Введите номер карты: '))
        card.isdigit()
        if card.isdigit == False:
            print('ты ввёл неверные данные')
        if len(card) !=16:
            print('ты ввёл недостаточно цифр')
            