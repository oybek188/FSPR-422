print("Задание №1")
print("""
Создать программу которая записывывает в список 10 словарей состоящий из двух ключей: "name" и "age"
и при этом используйте input и for.
Пример: Скажем у нас есть пустой список
info = []
На результат верунть список из 10 словарей, где каждый словарь состоит из ключей "name" и "age"

# Результат 
info = [ 
    { 
        "name": "fdffg", 
        "age": "12" 
    }, 
    { 
        "name": "fdffg", 
        "age": "12" 
    } 
]
""")

info = []
for i in range(10):
    info.append(
        {
            "name": input("input name: "),
            "age": int(input("input age: ")),
        }
    )
print(info)
