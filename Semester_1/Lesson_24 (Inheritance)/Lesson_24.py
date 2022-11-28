class Father:
    house = True

    def __init__(self, name, job, hobby, bank_accout):
        self.name = name
        self.job = job
        self.hobby = hobby
        self.bank_account = bank_accout

    def spend(self, amount):
        self.bank_account -= amount
    
    def income(self, amount):
        self.bank_account += amount

    cooked_food = ""
    def cook(self, products):
        if "carrot" in products and "rice" in products:
            self.cooked_food = "fathers plov"
        else:
            print("We can't cook with these products.")
            
class Mother:
    cooked_food = ""
    def cook(self, products):
        if "carrot" in products and "meat" in products and "rice" in products:
            self.cooked_food = "mothers plov"
        else:
            print("We can't cook with these products.")

class Child(Father, Mother):
    def __init__(self, name, job, hobby, bank_account, age):
        self.age = age
        super().__init__(name, job, hobby, bank_account)

    def cook(self, products):
        super().cook(products)
        if "масло" in products and "баклажан" in products and "помидор" in products:
            self.cooked_food = "жареный баклажан"

class ChildTwo(Father, Mother):
    pass

class ChildThird(Father, Mother):
    pass


child = Child("Oybek", "IT", "hiking", 100000, 35)
print(child.bank_account, child.hobby)
child.spend(200)
print(child.bank_account)
child.income(200)
print(child.bank_account)

child.cook(["масло", "баклажан", "помидор"])
print(child.cooked_food)
child.cook(["rice", "carrot"])
print(child.cooked_food)


child.cook(["carrot", "meat", "rice"])
print(child.cooked_food)


