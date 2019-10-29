import sys
import string


def word_filter(word_list):
    """ Remove all puncuations from the list"""
    words = word_list
    for index, word in enumerate(words):
        string_remove = str.maketrans(".,!:?", 5*" ")
        new_string = word.translate(string_remove)
        words[index] = new_string.strip()
    return words


def readFile():
    """ Returns a list filled with words"""
    file = open("corpes.txt", "r")
    words = []
    counter = 0
    dict_words = {}
    interations = 0
    for word in file.readlines():
        for element in word.split():
            words.append(element.lower())
            counter += 1
    words = word_filter(words)  # Filter out the words
    file.close()
    for letter in words:
        file = open("corpes.txt", "r")
        count = 0
        for data in file.readlines():
            count += data.lower().count(letter)
        interations += 1
        print("Out: ", interations)
        if letter not in dict_words:
            dict_words.update({letter: count})
    print("Total word count:", counter)
    return dict_words


def histogram(list_words):
    words = list_words
    words_2 = words
    # We will optimized the algorith later, brute force method for now
    dict_words = {}
    two_D = []
    # Begin Filter
    index = 0
    # End filterring
    for word in words:
        #checking = False
        counter = 0
        for word2 in words:
            if word2 == words:
                counter += 1
        index += 1
        print("Out ", index)
        #count = word.count
        if not word.lower() in dict_words:
            dict_words.update({word.lower(): counter})

    return dict_words


def unique_words(list_words):
    return len(list_words)


def frequency(desired_word, word_list):
    words = word_list
    for word in words:
        if word.lower() == desired_word.lower():
            return desired_word + " " + str(words[word])


def by_Amount(word_list, number_desired):
    words = word_list
    temp_list = []
    for word, index in words.items():
        if index == int(number_desired):
            temp_list.append(word)
    return temp_list


if __name__ == '__main__':
    params = sys.argv[1:]
    words = readFile()
    #words = histogram(words)
    # words = {"About": 2, "because": 1, "Jose": 1, "Name": 1, "cat": 1, "fish": 2}
    # print(f"This is the list of words:{words}")
    print(unique_words(words))
    print(frequency(input("Type desired word:"), words))
    print(by_Amount(words, input("Type desired number for words: ")))
