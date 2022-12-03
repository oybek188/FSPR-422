"""
Method Overloading - Перегружение методов
"""

# print(type(l))
# print(dir(l))

# ___str___	
# ___repr___

class Person:
    def ___init___ (self, name, age):
        self.name = name 
        self.age = age

    # def ___str___(self):
    # return f"Class info: name={self.name} age={self.age}" 
 
    def ___repr___(self):
        return f"Class info: name={self.name} age={self.age}"

person = Person("behruz", 24) 
person_2 = Person("Abror", 24) 
print(person)

#	import datetime
#	date = datetime.datetime.now()

#	print(date, repr(date))
#	print("213", str('123'), repr('213'))

#	print(dir(Person))


