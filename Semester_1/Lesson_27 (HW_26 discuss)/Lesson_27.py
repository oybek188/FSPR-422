
USERS = [
    {
        "name": "Bek",
        "password": "123456",
        "email": "bek@gmail.com",
        "purchases": [],
        "card": {"code": "1234567890123456", "money": 1000}
    }
]

class Store:
    pass

person_1 = Store()


class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.password = password
        self.email = email
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        for user in USERS:
            if user["email"] == email or user["password"] == password:
                return "Wrong email or password"
            else:
                break

        if not (name and  email and  password and  card_code and  card_balance):
            return "Empty values were given"

        if name.isalpha() and '@' in email and len(password) >= 6 and len(card_code) == 16:
            USERS.append(
                {
        "name": "Bek",
        "password": "123456",
        "email": "bek@gmail.com",
        "purchases": [],
        "card": {"code": "1234567890123456", "money": 1000}
                }
            )
            return cls(name, email, password, card_code, card_balance)
        else:
            return "Wrong credentials"

    @classmethod
    def login(cls, email, password):
        print("Login success")

enter_method = input('Choose: register or login: ')
if enter_method == "register":
    user_1 = Store.register("Oybek", "oybek@gmail.com", "12345678", "1234567890123456", 1000)
elif enter_method == "login":
    user_1 = Store.login("oybek@gmail.com", "12345678")

print(user_1)
print(user_1.name, user_1.email, user_1.password)
for user in USERS:
    print(user)

