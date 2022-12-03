
"""
Encapsulation (Инкапсуляция) - в информатике размещение в одном компоненте данных и методов, 
которые с ними работают. Также может означать скрытие каких-то данных, чтобы их не могли изменить или удалить. 
Например, доступ к скрытой переменной может предоставляться не напрямую,  
а с помощью методов для чтения и изменения её значения.
"""

class PlayerCharacter:
    # Class object attribute
    membership = True # доступ для всез образов класса
    def __init__(self, hobby, name='anonumous', age=0):
        self.name = name # attributes
        self.age = age
        self._hobby = hobby
    
    def shout(self): # method
        return f'My name is {self.name}'
    
    def _welcome(self):
        return "HEEEEEEEYYYYYY!"

    def shout2(self):
        return f'{self._welcome()}. My name is {self.name} and my hobby is{self._hobby}'

    @classmethod # Convert a function to be a class method.
    def adding_things2(cls, num1, num2): # cls - это сам класс
        # PlayerCharacter(num1 + num2)
        return cls(num1 + num2)

    @staticmethod # позволяет мотоду не иметь доступа к классу self
    def multiply(a, b):
        return a * b

player_1 = PlayerCharacter('Jerry', 20)
print(player_1.name, player_1.age)

player_1 = PlayerCharacter('Oybek')
print(player_1.name, player_1.age)

player_3 = PlayerCharacter.adding_things2(2, 20)
print("age =", player_3.age, "name =", player_3.name)

print(player_1.multiply(23, 43))
print(player_1.shout2())
print(player_1._welcome())

 
# draft - вес корабля 
# crew - пассажиры

# is_worth_it - создать метод, который возвращает True или False, если  
# вес корабля после того как вычесть количество пассажиров остается  
# равным 20 или больше, то вы возвращете True (его можно грабить) 
# каждый пассажир (crew) добавляет в вес корбался 1.5 единиц

class Ship: 
    def __init__(self, draft, crew): 
        self.draft = draft 
        self.crew = crew 
    
    def is_worth_it(ship):
        return 