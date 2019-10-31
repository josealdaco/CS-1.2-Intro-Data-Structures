import sys
import re
import random


def word_filter(word_list):
    """ Remove all puncuations from the list"""
    words = word_list
    for index, word in enumerate(words):
        string_remove = str.maketrans(".,!:?][@$ *()1234567890''#â€œXIV%-_`~^{}™  ", 43*" ")
        new_string = word.translate(string_remove)
        x = re.findall("mystery", new_string.strip())
        if len(x) != 0:
            print("This is whats inside of the new string mystery:", new_string)
        words[index] = new_string.replace(" ", "")
    return words


def histogram_Dictionary():
    """ Returns a Dictionary with the non duplicate word and count"""
    file = open("corpes.txt", "r")
    words = []
    counter = 0
    temp_count = 0
    dict_words = {}
    str = ""
    for word in file.readlines():
        str += word.lower()
        for element in word.split():
            words.append(element.lower())
            counter += 1
    file.close()
    words = word_filter(words)  # Filter out the words
    random.shuffle(words)  # Shuffle the words beforehand to save time complexity
    for word2 in words:
        word2.replace(" ", "")
        if word2 in dict_words:
            result = re.findall("mystery", word2)
            if(len(result) != 0):
                temp_count += 1
                print("Found a mystery", temp_count)
            value = dict_words.get(word2)
            result = re.findall(word2, word2)
            value += 1
            dict_words.update({word2: value})
        else:
            dict_words.update({word2: 1})

    return dict_words


def histogram_Lists():
        """ Returns a Lists of Lists with the non duplicate word and count"""
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
        words = word_filter(words)  # Filter out the words
        for word2 in words:
            list = re.findall(word2, str)
            result = False
            for list_word in list_words:
                if word.lower() in list_word:
                    result = True
            if result is False:
                list_words.append([word2, len(list)])
        file.close()
        return list_words


def unique_words(list_words):
    return len(list_words)


def frequency_Dictionary(desired_word, word_list):
    words = word_list
    for word in words:
        if word.lower() == desired_word.lower():
            return desired_word + " " + str(words[word])


def frequency_Lists(desired_word, word_list):
    words = word_list
    for word in words:
        for list_word in word:
            if list_word.lower() == desired_word.lower():
                return desired_word + " " + str(words[word])


def by_Amount(word_list, number_desired):
    words = word_list
    temp_list = []
    for word, index in words.items():
        if index == int(number_desired):
            temp_list.append(word)
    return temp_list


def sampler_Dictionary(dict_list):
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
            break
    return sentence # Just getting one word


def test_prob(dict_list, amount):
    dict_copy = dict_list
    for _ in range(int(amount)):
        #sentence = sampler_Dictionary(["one":1, "fish":, "two", "fish", "red", "fish", "blue", "fish"])
        sentence = sampler_Dictionary(dict_list)
        print("this is the sentence:", sentence)
        str = read_Sentence(sentence)
        print(str)
        #file_append(str)


def read_Sentence(sentence_list):
    str = ""
    for word in sentence_list:
        str += word
    return str


def file_append(str):
    file = open("test_file.txt", "a+")
    file.write(str + "\n")

if __name__ == '__main__':
    params = sys.argv[1:]
    words = histogram_Dictionary()
    #words = histogram_Lists()
    #print(words)
    # words = {"About": 2, "because": 1, "Jose": 1, "Name": 1, "cat": 1, "fish": 2}
    # print(f"This is the list of words:{words}")
    print(unique_words(words))
    #print(frequency_Lists(input("Type desired word:"), words))
    # sentence = sampler_Dictionary(words)
    test_prob(words, 100)
    #print(by_Amount(words, input("Type desired number for words: ")))
    while True:
        print(frequency_Dictionary(input("Type desired word:"), words))
        x = input("Do you wish to continue? [Y/N]").lower()
        if x == "n":
            break
