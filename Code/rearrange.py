import sys
from random import randint
""" Simple program that randomizes the words inputted and outputs them in the console.
    Edge cases such as determinating wheather result is an int or not is not added yet"""

if __name__ == "__main__":
    params = sys.argv[1:]
    words_list = []
    for word in params:
        words_list.append(word)
    print("Reading words in order but randomized")
    chosen = []
    for index in range(len(words_list)):
        pick = randint(0, len(words_list) - 1)
        while True:
            result = False
            for x in chosen:
                if x == pick:
                    result = True
            if result is False:
                print(words_list[pick], end=" ")
                chosen.append(pick)
                break
            else:
                pick = randint(0, len(words_list) - 1)

    # print("\nReading words in reverse")
    # last_index = len(words_list) - 1
    # while last_index >= 0:
    #     print(words_list[last_index], end=" ")
    #     last_index -= 1
