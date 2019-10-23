import sys
from random import randint
""" Simple program that randomizes the words inputted and outputs them in the console.
    Edge cases such as determinating wheather result is an int or not is not added yet"""

if __name__ == "__main__":
    params = sys.argv[1:]
    words_list = []
    for index in range(len(params)):
        words_list.append(params[randint(0, len(params) - 1)])
    for i in words_list:
        print(i, end=" ")
