# class Marker:
    # peremennaya = atribut
    # funksiya = metod
    # def __init__(self, company,):
    #     self.company = company
    #     self.color = color
    
# marker = Marker("Marker inc.", )

# print(dir(marker))
# print(dir(obj))
# print(type(a))

# class Marker:
#     size = 15
# def __init__(self, company, color, price):
#         self.company = company
#         self.color = color
#         self.price = price 

# marker = Marker("Marker inc.", "blue", 12 )
# marker_2 = Marker("Market inc.", "black", 10 )
# marker_3 = Marker("Mar inc.", "red", 8 )

# print(marker.company)
# print(marker.color)
# print(marker.price)
# print(marker.size)

class Marker:
    size = 15
    health = 10
    def __init__(self, company, color, price):
        self.company = company
        self.color = color
        self.price = price
    def draw(self, line_length):
        
            return "Marker istoshen"
            self.health -= line_length

marker = Marker("Marker inc.", "blue", 12 )
marker_2 = Marker("Market inc.", "black", 10 )
marker_3 = Marker("Mar inc.", "red", 8 )


print("health =", marker.health)
marker.draw(11)
print("health =", marker.health)
marker.draw(5)
print("health =", marker.health)
print(marker.draw(5))
print("health =", marker.health)


# marker = Marker("Marker inc.", "blue", 12 )
# marker_2 = Marker("Market inc.", "black", 10 )
# marker_3 = Marker("Mar inc.", "red", 8 )

