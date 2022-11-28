# Функции

if 1 == 1:
    print(True)

def greet():
    print("Hello")

#вызов функции
print("вызов фунции", greet())

def greet():
    return "Hello" # return - вернуть

result = greet()
print(result)

def greet(name): # аргумент функции
    print(f"Hello {name}")

# greet("Behruz")
# s = "Bekzod"
# greet(s) # Bekzod
# greet( input("Input name:"))

def greet(name): # аргументы функции
    return f"Hello {name}"

print(greet("Jamshid"))
result = greet("Oybek")
print(result)

# Написать функцию, которая принимает список фарангейтов и возвращает список цельсия 
faranheits = [30, 20, 19, 24, 45] 
def fars_to_cels(faranheits):
    result = []
    for far in faranheits: 
        celsius = (far - 32) * 5 / 9  
        result.append(celsius)
    return(result)
print(fars_to_cels(faranheits))


square_line = 4
star = "*" 
def draw_square(square_line, star):
    for i in range(square_line):
        if i > 0 and i < (square_line -1):
            empty_space = " " * (square_line -2)
            print(f"{star}{empty_space}{star}")
        else:
            print(star * square_line)
draw_square(5, "*")
