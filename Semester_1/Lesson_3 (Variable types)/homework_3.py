print("Использование метода capitalize")
a = 'HeLLo WoRLd!'
print(a.capitalize())
print(sep="\n\n")

print("Использование метода lower")
b = 'HeLLo WoRLd!'
print(b.lower())
print(sep="\n\n")

print("Использование метода upper")
c = 'HeLLo WoRLd!'
print(c.upper())
print(sep="\n\n")

print("Использование метода find")
#Метод find() возвращает индекс первого вхождения подстроки (если найден). Если не найден, возвращается -1.
str="Bobir Akilkhanov Tech Academy"
d=str.find("n")
print("index is:", d)
print(sep="\n\n")

print("Использование метода isdigit")
#Метод isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False
e = "1234567890"
print("Characters are digits in e:", e.isdigit())
f = "Bobir Akilkhanov Tech Academy"
print("Characters are digits in f:", f.isdigit())
print(sep="\n\n")

print("Использование метода join")
#Строковый метод join() возвращает строку, объединяя все элементы итерации, разделенные разделителем строк.
test = {'2', '1', '3'} 
s = ', ' 
print(s.join(test)) 

test = {'Python', 'Java', 'Ruby'} 
s = '->->' 
print(s.join(test))
print(sep="\n\n")

print("Использование метода index")
#Метод str.index() возвращает индекс подстроки внутри строки (если она найдена). Если подстрока не найдена, возникает исключение.
sentence = 'Bobir Akilkhanov Tech Academy' 
result = sentence.index('Tech') 
print("Substring 'Tech':", result) 
result = sentence.index('Python') 
print("Substring 'Python':", result)

