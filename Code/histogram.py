import sys
import re
import random
import string


def file_append(str):
    file = open("test_file.txt", "a+")
    print(str)
    file.write(str + "\n")


def word_filter(word_list):
    """ Remove all puncuations from the list"""
    words = word_list.copy()
    if len(word_list) != 0:
        for index, word in enumerate(words):
            new_string = word.translate({ord(i): '' for i in """,?!,":;@$*[.][]#()~``,â€œâ™"""})
            new_string = new_string.replace(" ", "")  #  translate({ord(i): ' ' for i in """"""})
            new_string = new_string.strip()
            new_string = ''.join([x for x in new_string if x in string.printable])
            words[index] = new_string.lower()
            return words


def histogram_Dictionary(word_list):
    """ Returns a Dictionary with the non duplicate word and count"""
    words = []
    counter = 0
    dict_words = {}
    str = ""
    for word in word_list:
        str += word.lower()
        for element in word.split():
            words.append(element.lower())
            counter += 1
    words = word_filter(words)  # Filter out the words
    random.shuffle(words)  # Shuffle the words beforehand to save time complexity
    for word2 in words:
        word2.replace(" ", "")
        if word2 in dict_words:
            value = dict_words.get(word2)
            value += 1
            dict_words.update({word2: value})
        else:
            dict_words.update({word2: 1})

    return dict_words


def histogram_Lists():
        """Returns a Lists of Lists with the non duplicate word and count"""
        file = open("corpes.txt", "r")
        words = []
        counter = 0
        list_words = []
        str = ""
        for word in file.readlines():
            str += word.lower()
            for element in word.split():
                words.append(element.lower())
                counter += 1
        file.close()
        words = word_filter(words)  # Filter out the words
        print("words filtered")
        list_words.append([words[0], 0])
        for word2 in words:
            index = 0
            for words_list in list_words:
                if words_list[0] == word2:
                    words_list[1] += 1
                    break
                elif words_list[0] != word2 and index == len(list_words) -1:
                    list_words.append([word2, 0])
                index += 1
        return list_words


def unique_words(list_words):
    return len(list_words)


def unique_words_List(list_of_lists):
    return len(list_of_lists)


def frequency_Dictionary(desired_word, word_list):
    words = word_list
    for word in words:
        if word.lower() == desired_word.lower():
            return desired_word + " " + str(words[word])


def frequency_Lists(desired_word, word_list):
    words = word_list.copy()
    for word in words:
        if word[0].lower() == desired_word.lower():
            return desired_word + " " + str(word[1])


def by_Amount(word_list, number_desired):
    words = word_list
    temp_list = []
    for word, index in words.items():
        if index == int(number_desired):
            temp_list.append(word)
    return temp_list


def sampler_Dictionary_word(dict_list):
    """     Function returns a word   """
    new_list = dict_list.copy()
    total = sum(new_list.values())  # Getting all values
    result = random.randint(1, total)  # Random value from 1 to totalValues
    for word in list:
        if result - new_list[word] <= 0:
            return word
        result -= new_list[word]


def sampler_Dictionary_sentence(dict_list):
    """     Function returns a sentence    """
    dict_copy = dict_list.copy()
    total_words = len(dict_copy)  # Find total
    sentence = []

    # Find the max of the word list
    max = 0
    for word3 in dict_copy:
        value = dict_copy.get(word3)
        if value >= max:
            max = value

    for word in dict_copy:  # Find value and convert to percentage
        value = dict_copy.get(word)
        percentage = value/total_words
        dict_copy.update({word: percentage})

    for word_2 in dict_copy:
        # 1 is hardcoded because you cannot have a number less then 1
        result = random.uniform(0.0, 1.0)
        value = dict_copy.get(word_2)
        if value >= result:
            sentence.append(word_2)
    return sentence  # Just getting one word


def test_prob_sentence(dict_list, amount):
    for _ in range(int(amount)):
        sentence = sampler_Dictionary_sentence(dict_list)
        str = read_Sentence(sentence)
        print(str)


def test_prob_single_word(dict_list, amount):
    for _ in range(int(amount)):
        sentence = sampler_Dictionary_word(dict_list)
        str = read_Word(sentence)
        print(str)


def read_Word(sentence_list):
    str = ""
    for word in sentence_list:
        str += word
    return str


def read_Sentence(sentence_list):
    str = ""
    for word in sentence_list:
        str += word + " "
    return str


if __name__ == '__main__':
    params = sys.argv[1:]
    test_list = [[2, 1], [0, 34]]
    words = histogram_Lists()
    print(unique_words_List(words))   # Fix unique words
    print(frequency_Lists(input("Type desired word: "), words))
    #test_prob_single_word(words, 10)
    #test_prob_sentence(words, 5)
    #while True:
    #    print(frequency_Dictionary(input("Type desired word:"), words))
    #    x = input("Do you wish to continue? [Y/N]").lower()
    #    if x == "n":
    #        break
