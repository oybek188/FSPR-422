import numbers

# a, b, *args = (2, 4, 4, 7, 8, 9, 0)
# print(a, b, args)


# print("range 1")
# for i in range(10): # 0-9
#     print(i)

# print("range 2")
# for i in range(4, 10): # 4-9
#     print(i)

# print("range 3")
# for i in range(4, 10, 2): # 4-9 # 2 - это цикл
#     print(i)

# print("list")
# numbers = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(numbers)):
#     numbers[i] *=4
# print(numbers)


# continue / break / pass

print("Continue")
numbers = [1, 2, 3, 5, 4, 5, 6, 7]
for val in numbers:
    if val == 5 or val == 7: # val = 5
        print(f"пропустить {val}")
        continue # -> for
    print("val =", val)

print("Break")
numbers = [1, 2, 3, 5, 4, 5, 6, 7]
for val in numbers:
    if val == 5 or val == 7: # val = 5
        print(f"выйти из цикла {val}")
        break # -> for
    print("val =", val)

print("Pass")
if 1 == 1:
    pass # пропускает, когда if ждет дальнейшей команды, например print

