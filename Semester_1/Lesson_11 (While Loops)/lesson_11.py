# **** 
# *  * 
# *  * 
# **** 
# square_line = 4 
# star = "*" 
# star_width = star * square_line 
# print(star_width) 
# print(f"{star}  {star}") 
# print(f"{star}  {star}") 
# print(star_width)


square_line = 4
star = "*" 
for i in range(square_line):
    if i > 0 and i < (square_line -1):
        empty_space = " " * (square_line -2)
        print(f"{star}{empty_space}{star}")
    else:
        print(star * square_line)

# i = 0
# while i < 10: # True - while будет работать
#     print("i=", i) # 9
#     i += 1 # 9 + 1 = 10
# i = 0
# while True:
#     i += 1
#     print("i =", i)
#     if i == 100:
#         break

# names = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < len(names): # 6
#     print(names[i])
#     i +=1

# s = "ABCDEFG"
# for i in range(len(s)):
#     s[i]

# for i, val in enumerate("ABCDEFG"):
#     print(i, val)
