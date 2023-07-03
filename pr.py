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
