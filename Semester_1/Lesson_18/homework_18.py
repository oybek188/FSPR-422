# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/solutions/python
def abbrevName(name):
    x = name
    y = name.split()
    return y[0][0].upper() + "." + y[1][0].upper()


# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
def add_length(s: str) -> list:
    words_with_len = []
    for i in s.split():
        words_with_len.append(i + ' ' + str(len(i)))
    return words_with_len


# https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
def area_or_perimeter(l , w):
    if l == w:
        ap = l * w
    else:
        ap = l * 2 + w * 2
    return ap