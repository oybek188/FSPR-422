# square_line = 4
# star = "*" 
# for i in range(square_line):
#     if i > 0 and i < (square_line -1):
#         empty_space = " " * (square_line -2)
#         print(f"{star}{empty_space}{star}")
#     else:
#         print(star * square_line)

text = "codewars" # csordaew
l = int(len(text))
s = text
i = l-1
while i > -1: # 6
    print(s[i], end=' ')
    i -= 1


# for i in range(len(s)):
#     print(s[0] + s[-1], end=' ')
    # i + 1

# while i < len(text): # 6
#     print(text[i])
#     i +=1

# for i in len(s):
#     if i > 0:
#         print(s[1] + s[2])



#     * 
#    *** 
#   *****
# x = 5
# for i in range(x):
#     print(' ' * (x-i-1) + '*' * (i*2+1))
# print(' ' * (x-2), '*')
# print(' ' * (x-2), '*')
