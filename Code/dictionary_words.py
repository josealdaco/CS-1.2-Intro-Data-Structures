import sys
from random import randint


def get_words(index):
    """ In this program I am looping the amount of words desired.
        I open the file once to get a random index and open it once again to
        loop over the file once more. I then print the random words into a single line,
        and placing a period at the end of the final word"""
        
    index = int(index)
    words = []
    indicator = 0
    for _ in range(index):
        if index > 0:
            random_index = randint(0, len(open("/usr/share/dict/words", "r").readlines()) - 1)
        else:
            random_index = 0
        for word in open("/usr/share/dict/words", "r").readlines():
            if indicator == random_index:
                words.append(word[0:len(word) - 1])
                break
            indicator += 1
        indicator = 0
    for pick in words:
        if pick == words[len(words) - 1]:
            print(pick + '.', end=" ")
        else:
            print(pick, end=" ")


if __name__ == "__main__":
    params = sys.argv[1:]
    get_words(params[0])
