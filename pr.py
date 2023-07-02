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
def calclis(nums, d):
    w = []
    for i in nums:
       if i not in d:
           if i not in w:
               

                w.append(i)
    return w


print(calclis(['s', 'sooliman', 'l'], ['l', 's', '', 'sooliman']))
# print(dir(list))
s = "HELLO world"

print(s[::-1])
