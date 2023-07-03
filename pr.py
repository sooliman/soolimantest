# # The class defines a computer object with a private maximum price attribute that can be set and
# # retrieved using methods.
# class Computer:

#     def __init__(self):
#       """
#       This is a Python class with methods to set and print the maximum selling price of a product.
#       """
#       # `self.__maxprice = 900` is initializing a private attribute `__maxprice` with a value of 900
#       # for the `Computer` class. The double underscore prefix before the attribute name makes it
#       # private, which means it can only be accessed within the class and not from outside the class.
#       self.__maxprice = 900

#     def sell(self):
#       print(f'Selling Price: {self.__maxprice}')

#     def setMaxPrice(self, price):
#       """
#       This function sets the maximum price for an object.

#       :param price: The "price" parameter is a value that is passed to the "setMaxPrice" method. It is
#       used to set the value of the "__maxprice" attribute of the object that the method is called on. The
#       "__maxprice" attribute is likely a private attribute that is used to store the
#       """# `self.__maxprice = price` is a method in the `Computer` class that sets the value of the
#       # private attribute `__maxprice` to the value passed as the `price` parameter. This method is
#       # used to update the maximum selling price of the computer object. By using a method to set
#       # the value of the private attribute, the class can control how the attribute is modified and
#       # ensure that it is only modified in a safe and controlled manner.

#       self.__maxprice = price

# c = Computer()
# c.sell()

# # change the price
# c.__maxprice = 1000
# c.sell()

# # using setter function
# c.setMaxPrice(1000)
# c.sell()

# import timeit


# def abbrevName(name):
#     initials = [word[0].upper() for word in name.split()]
#     return '.'.join(initials)


# def abbrev_name(name):
#     return f'{name[0].capitalize()}.{name[name.index(" ")+1].capitalize()}'


# # قياس وقت تنفيذ الدالة abbrevName()
# time_abbrevName = timeit.timeit(
#     "abbrevName('Sam Harris')", setup="from __main__ import abbrevName", number=100000)
# # قياس وقت تنفيذ الدالة abbrev_name()
# time_abbrev_name = timeit.timeit(
#     "abbrev_name('Sam Harris')", setup="from __main__ import abbrev_name", number=100000)

# # طباعة نتائج القياس
# print(f"وقت تنفيذ الدالة abbrevName(): {time_abbrevName} ثانية")
# print(f"وقت تنفيذ الدالة abbrev_name(): {time_abbrev_name} ثانية")

# ...
# def calclis(nums, d):
#     w = []
#     for i in nums:
#        if i not in d:
#            if i not in w:


#                 w.append(i)
#     return w


# print(calclis(['s', 'sooliman', 'l'], ['l', 's', '', 'sooliman']))
# # print(dir(list))
# s = "HELLO world"

# print(s[::-1])
import mysql.connector


# def final_grade(e, p):
#     return 100 if e in range(91, 101) or p >= 10 else 90 if e in range(76, 91) or p in range(5, 9) else 75 if e in range(50, 76) or p in range(2, 4) else 0


# print(final_grade(5, 3))
# print(dir(int))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__',
# '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__'
# , '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__',
# '__rand__', '__rdivmod__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rfloordiv__',
# '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__',
# '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
# '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
# '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate',
# 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# p = '200'
# print(p[::-1])


# def to_industrial(time):
#     return


# def to_normal(time):
#     return ''.join(time.replace('.',':'))
# print(to_normal(0.33))

# g = 4
# h = 0.00
# for i in range(1, g):
#     if i % 2 == 0:
#         print(i)
#         h += 0.02
#     elif i % 2:
#         # print(i)
#         h += 0.03
# print(h)
# print(2 % 2 == 0)
# print(5/60
#       )
# d = "'2'.0/60"
# o = f'{d:.1}'
# print(o == str(o))


def to_industrial(time):
    if isinstance(time, str):
        h, m = map(int, time.split(':'))
        print(h)
        time = 60*h + m
        print(time)
    return round(time/60, 2)


y = 27
i = []
while 1 < y:

    if y % 2 == 0:

        y /= 2
        i.append(y)

    elif y % 2 != 0:
        y = y*3+1
        i.append(y)
print(len(i))


def uni_total(s):
    # your code here
    return sum((ord(s) for s in s)) or 0


print(uni_total(""))


def describe_age(a):
    return f"You're a(n) {a<13 and 'kid' or a<18 and 'teenager' or a<65 and 'adult' or 'elderly'}"
# describe_age=lambda n:"You're a(n) "+"kid teenager adult elderly".split()[(n>12)+(n>17)+(n>64)]


print(describe_age(9))


def subtract_sum(num):
    i = {1: 'kiwi', 2: 'pear', 3: 'kiwi', 4: 'banana', 5: 'melon', 6: 'banana', 7: 'melon', 8: 'pineapple', 9: 'apple', 10: "pineapple", 11: "cucumber", 12: "pineapple", 13: "cucumber", 14: "orange", 15: "grape", 16: "orange", 17: "grape", 18: "apple", 19: "grape", 20: "cherry", 21: "pear", 22: "cherry", 23: "pear", 24: "kiwi", 25: "banana", 26: "kiwi", 27: "apple", 28: "melon", 29: "banana", 30: "melon", 31: "pineapple", 32: "melon", 33: "pineapple", 34: "cucumber", 35: "orange", 36: "apple", 37: "orange", 38: "grape", 39: "orange", 40: "grape", 41: "cherry", 42: "pear", 43: "cherry", 44: "pear", 45: "apple", 46: "pear", 47: "kiwi", 48: "banana", 49: "kiwi", 50: "banana", 51: "melon", 52: "pineapple", 53: "melon", 54: "apple", 55: 'cucumber', 56: 'pineapple', 57: 'cucumber', 58: 'orange', 59: 'cucumber', 60: 'orange', 61: 'grape', 62: 'cherry', 63: 'apple', 64: 'cherry', 65: 'pear', 66: 'cherry', 67: 'pear', 68: 'kiwi', 69: 'pear', 70: 'kiwi', 71: 'banana', 72: 'apple', 73: 'banana', 74: 'melon', 75: 'pineapple', 76: 'melon', 77: 'pineapple', 78: 'cucumber', 79: 'pineapple', 80: 'cucumber', 81: 'apple', 82: 'grape', 83: "orange", 84: "grape", 85: "cherry", 86: "grape", 87: "cherry", 88: "pear", 89: "cherry", 90: "apple", 91: "kiwi", 92: "banana", 93: "kiwi", 94: "banana", 95: "melon", 96: "banana", 97: "melon", 98: "pineapple", 99: "apple",
         100: "pineapple"}
    # t = 325
    if num <= 100:
        return i[num - sum(map(int, str(num)))]
    else:
        while num >= 100:
            r = sum(map(int, str(num)))
            num -= r

        return (i[num])


# print(subtract_sum(899))
fruits = {'kiwi':      [1, 3, 24, 26, 47, 49, 68, 70, 91, 93],
          'pear':      [2, 21, 23, 42, 44, 46, 65, 67, 69, 88],
          'banana':    [4, 6, 25, 29, 48, 50, 71, 73, 92, 94, 96],
          'melon':     [5, 7, 28, 30, 32, 51, 53, 74, 76, 95, 97],
          'pineapple': [8, 10, 12, 31, 33, 52, 56, 75, 77, 79, 98, 100],
          'apple':     [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],
          'cucumber':  [11, 13, 34, 55, 57, 59, 78, 80],
          'orange':    [14, 16, 35, 37, 39, 58, 60, 83],
          'grape':     [15, 17, 19, 38, 40, 61, 82, 84, 86],
          'cherry':    [20, 22, 41, 43, 62, 64, 66, 85, 87, 89]}
for fruit, numbers in fruits.items():
    if 10 in numbers:
        print(fruit)
