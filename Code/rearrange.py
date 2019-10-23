import sys
from random import randint
""" Simple program that randomizes the words inputted and outputs them in the console.
    Edge cases such as determinating wheather result is an int or not is not added yet"""


def update(index, list, value):
    list = list
    print("This is the list at first", list)
    list[index] = value
    print("This is after updating value:", list)
    return list

def rearrange(sentence):
    words_list = []
    final_result = ""
    for word in sentence:
        words_list.append(word)
    print("Reading words in order but randomized")
    chosen = []  # Since i can't define the size of list
    for index in range(len(words_list)):
        pick = randint(0, len(words_list) - 1)
        while True:
            result = False
            for x in chosen:
                if x == pick:
                    result = True
            if result is False:
                # print(words_list[pick], end=" ")
                final_result += words_list[pick] + " "
                chosen.append(pick)
                #update(chosen[index], words_list, words_list[pick])
                break
            else:
                pick = randint(0, len(words_list) - 1)
    print(final_result)
if __name__ == "__main__":
    params = sys.argv[1:]
    sentence = "Flying bats and scary cats"
    word = sentence.split()
    rearrange(word)
    print("\nNow we will print these in reverse")
    #last_index = len()-1
    #print(last_index)
    sentence = ""
    #print("This is the worlds list:", words_list)
    # print("\nReading words in reverse")
    # last_index = len(words_list) - 1
    # while last_index >= 0:
    #     print(words_list[last_index], end=" ")
    #     last_index -= 1
