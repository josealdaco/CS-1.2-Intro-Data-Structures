import sys
from random import randint


def get_words(index):
    amount = int(index)
    file = open("words.txt", "r")
    words = {}
    for index_2, word in enumerate(file.readlines(), start=1):
        words.update({index_2: word[0:len(word) - 1]})
    file.close()
    result = ""
    for counter in range(amount):
        result += words[randint(0, len(words) - 1)] + " "
    print(result)


if __name__ == "__main__":
    params = sys.argv[1:]
    get_words(params[0])
