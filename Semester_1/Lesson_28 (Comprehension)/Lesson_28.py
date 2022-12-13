# Comprehension

# Обычный цикл
numbers = []
for i in range(10):
    numbers.append(i)

print(numbers)


# Использование Comprehension
numbers = [i*5 for i in range(10)]
print(numbers)


# Использование Comprehension с функцией 
def multiply(i):
    return i*5

numbers = [multiply for i in range(10)]
print(numbers)


# 1 if 1 == 1 else False
numbers = [i*5 if i > 5 else False for i in range(10)]  # list
print(numbers)


text = (("Hi", "Steve!"), ("What's", "Up?"))
print([word for sentence in text for word in sentence])


numbers = tuple(i*5 for i in range(10))
print(numbers)

numbers = {i*5 for i in range(10)}
print(numbers)

numbers = {i:i*5 for i in range(10)}
print(numbers)
