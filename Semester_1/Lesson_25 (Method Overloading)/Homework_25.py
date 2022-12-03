class Person:
    def	__init__(self, x=0, y=9):
        self.x = x 
        self.у = y

    def	__sub__(self, other):
        x = self.x - other.x 
        у = self.у - other.у 
        return Person(x, y)

    def	__mull__(self, other):
        x = self.x * other.x 
        у = self.у * other.у 
        return Person(x, y)

    def __It__(self, other): #	<
        self_mag = (self.x * 2) + (self.у * 2)
        other_mag = (other.x * 2) + (other.у * 2)
        return self_mag < other_mag
        return self.x < other.x and self.у < other.у

    def __eq__(self, other):
        self_mag = (self.x * 2) + (self.у * 2) 
        other_mag = (other.x * 2) + (other.у * 2)
        return self_mag == other_mag

person = Person(230, 344) 
person_1 = Person(23, 34) 
person + person_1 # 
result = person < person_1 
print(result.x, result.y)
