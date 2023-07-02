import re
from functools import reduce as ree


def count_letter(string) -> str | int | list:
    """
    The function counts the number of characters in a given string or integer input.

    :param string: The input string that we want to count the number of characters in
    :return: the count of characters in the input string.
    """
    count = 0
    if type(string) == int:
        string = str(string)
    for i in string:
        count += 1
    return count

# # ===================================
# # ===        end fonction count_letter                     -==
# # ====================================

# # =======================
# # ===Start Str_of_list===
# # =======================
# # The `str_of_list` function takes a list as input (`Of_list`) and returns a string that
# # contains all the elements of the input list.


# def str_of_list(Of_list) -> str:
#     resul = []
#     if type(Of_list) == int:
#         Of_list = str(Of_list)
#         for i in range(count_letter(Of_list)):
#             resul.append(int(Of_list[i]))
#         return resul
#     else:
#         for i in range(count_letter(Of_list)):
#             resul.append(Of_list[i])
#         return resul


# # =======================
# # ===End Str_of_list===
# # =======================
# def str_zfill(txt: str, width: int, fillz) -> str:
#     return str(fillz)*(width-count_letter(txt))+txt


# def strip_str(stre: str, s: str = '') -> str:
#     # return stre.(s)
#     resul = []
#     for d in stre:
#         d.split()
#         if d != s:
#             resul.append(d)

#     return "".join(resul)
# # ===============================
# # ========     ???     ==========
# # ===============================


# def find_average(numbers):
#     """
#     The function "find_average" takes a list of numbers as input, calculates the sum of the numbers, and
#     returns the average of the numbers.

#     :param numbers: a list of numbers for which we want to find the average
#     :return: the average (mean) of the numbers in the input list.
#     """

#     return sum(numbers)/len(numbers)


# def powers_of_two(n):
#     return [2**x for x in range(n+1)], print(range(n))


# print(powers_of_two(3))
# #    l
# #     return [i* for i in range(1,len(n))]
# # n = 4
# # result = []
# # cont = 1
# # for i in range(1, n+1):


# def count_squares(cuts: int):
#     """
#     The function calculates the total number of squares that can be formed by making cuts on a square
#     sheet of paper.

#     :param cuts: The parameter "cuts" represents the number of cuts made to a square cake. The function
#     "count_squares" calculates the total number of squares that can be formed by making these cuts,
#     including the original square cake
#     :type cuts: int
#     :return: The function `count_squares` is returning the total number of squares that can be formed by
#     making `cuts` number of cuts on a square grid.
#     """
#     return 2 * (cuts + 1) * (cuts + 1) + 2 * (cuts + 1) * (cuts - 1) + 2 * (cuts - 1) * (cuts - 1)


# def count_squares(x):
#     """
#     The function calculates the number of squares in a given grid size.

#     :param x: The input parameter for the function "count_squares". It is a number that is used in the
#     calculation of the output value
#     :return: The function `count_squares` is returning the value of `6 * x**2 + 2`.
#     """

#     return 6 * x**2 + 2


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         self.x = x
#         return (True if selfx[0] == x[-1] else False)

# g = Solution()
# print(g.isPalindrome(121))


def romanToInt(s: str) -> int:
    f = {
        "I": 1,
        "V": 5,
        "XC": 90,
        'X': 10,
        "L": 50,
        "C": 100,
        'D': 500,
        'M': 1000,
        'CM': 900
    }
    f = f.replace()
    d = 0
    for i in s:
        d += f[i]
    return d


    """
    The function "rps" takes two inputs representing rock-paper-scissors moves and returns the winner or
    a draw.
    
    :param p1: "paper"
    :param p2: The parameter "p2" represents the choice of the second player in a game of
    rock-paper-scissors
    :return: The function `rps` is returning the result of the game of rock-paper-scissors between two
    players. In this specific case, it is returning "Player 2 won!" because "scissors" beats "paper".
    """
var = ["rock", "scissors", "paper"]
ans = ["Draw!", "Player 2 won!", "Player 1 won!"]

def rps(p1, p2):
    # The line `return ans[var.index(p1) - var.index(p2)]` is implementing the logic for a game of
    # rock-paper-scissors. It takes in two inputs `p1` and `p2`, representing the moves of two
    # players, and returns the result of the game.
    print(var.index(p1) - var.index(p2))
    return ans[var.index(p1) - var.index(p2)]

print(rps("scissors","paper"))
# print(romanToInt("MCMXCIV"))

# Regex Cheat sheet : https://www.dataquest.io/blog/regex-cheatsheet/
# Regex python tester : https://pythex.org/
# re doc : https://docs.python.org/3/library/re.html


# def roman_to_integer(s):
#     roman_values = {jh
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }

#     total = 0
#     previous_value = 0

#     # تحويل الرموز الرومانية إلى أرقام
#     for i in range(len(s)):
#         current_value = roman_values[s[i]]

#         # إذا كانت القيمة المقابلة للحرف أكبر من القيمة السابقة، قم بالجمع والطرح
#         if current_value > previous_value:
#             print("#"*30)
#             total += current_value - (2 * previous_value)
#             print(current_value)
#             print(previous_value)
#             print(total + current_value - (2 * previous_value))
#             print("#"*30)
#         else:
#             print('@'*20)
#             total += current_value
#             print(total)
#             print('@'*20)
#         previous_value = current_value
#     return total


# # print(roman_to_integer("MCMXCIV"))
# def calculetList(lis1: list, lis2: list):
#     lis3 = (lis1 + lis2)
#     # lis3.sort()
#     return (lis3)


# print(calculetList([], []))
# # someone => Parameter


# def say_hello_to(someone): {
#     print(f"Hello {someone}")
# }


# say_hello_to('ss     ')
# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

# class Member:

#     def __init__(self, name):

#         self.__name = name  # Private

#     def say_hello(self):

#         return f"Hello {self.__name}"

#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         lis3 = nums+target
#         lis3.sort()
#         return lis3

#     def get_name(self):  # Getter

#         return self.__name

#     def set_name(self, new_name):

#         self.__name = new_name


# one = Member("Ahmed")

# one._Member__name = "Sayed"
# print(one._Member__name)

# print(one.get_name())
# one.set_name('Abbas')
# print(one.get_name())
# print(one.twoSum([1, 2, 3], [1, 2, 3]))


# def twoSum(nums: list[int], target: int) -> list[int]:

#     hashmap = {}
#     for i in range(len(nums)):
#         # print(i)
#         hashmap[nums[i]] = i
#     for i in range(len(nums)):
#         # print(i)
#         complement = target - nums[i]
#         if complement in hashmap and hashmap[complement] != i:
#             print(i, hashmap[complement])
#             return [i, hashmap[complement]]
#     print(hashmap[complement])


# print(twoSum([  2,1,1, 3, 8, 2, 11], 3))
