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
        # Looping over amount desired
        if index > 0:
            random_index = randint(0, len(open("/usr/share/dict/words", "r").readlines()) - 1)  # Collecting random index
        else:
            random_index = 0
        for word in open("/usr/share/dict/words", "r").readlines():  # Opening file
            if indicator == random_index:  # Check if the index matches the indicator
                words.append(word[0:len(word) - 1])  # If so append the word from the index given
                break
            indicator += 1
        indicator = 0  # Reset indicator to 0 everytime
    result = ""
    for pick in words:
        if pick == words[len(words) - 1]:
            result += pick + "."
        else:
            result += pick + " "
    print(result)


if __name__ == "__main__":
    params = sys.argv[1:]
    get_words(params[0])
