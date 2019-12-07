import string
import random

""" Make sure to have an edge case if markov word has None """


def sample(dict):
    """Return a word from this histogram, randomly sampled by weighting
    each word's probability of being chosen by its observed frequency."""
    total = sum(dict.values())  # Getting all values
    result = random.randint(1, total)  # Random value from 1 to totalValues
    for word in dict:
        if result - dict[word] <= 0:
            return word
        result -= dict[word]


def nestedList(value, list):
    """ Finds index of nested list"""
    index = 0
    for items in list:
        if items[0] == value:
            return index
        index += 1
    return None


def sample_v2(chain, chainList):
    """Return a word from this histogram, randomly sampled by weighting
    each word's probability of being chosen by its observed frequency."""
    total = 0
    dict = chain[0]
    for item in chainList:
        total += chain[0].get(item)
    result = random.randint(1, total)  # Random value from 1 to totalValues
    for word in chainList:
        if result - dict[word] <= 0:
            return word
        result -= dict[word]


def word_filter(word_list):
    """ Remove all puncuations from the list"""
    words = word_list.split()
    if len(word_list) != 0:
        for index, word in enumerate(words):
            new_string = word.translate({ord(i): '' for i in """,?!,":;@$*[.][]#()~``,â€œâ™"""})
            new_string = new_string.replace('', "")  #  translate({ord(i): ' ' for i in """"""})
            new_string = new_string.strip()
            new_string = ''.join([x for x in new_string if x in string.printable])
            words[index] = new_string.lower()
    return words


def listToString(list):
    """ Converts list to string"""
    str = ""
    endPoint = 0
    for item in list:
        if endPoint < len(list):
            str += item + " "
        endPoint += 1
    return str


def markov_chain_v2(key, chain):
    """ Creating a mokup of the histogram n state """
    chainList = chain[1].get(key)
    if chainList is None:
        return "."  # If that word has no next one
    else:
        return sample_v2(chain, chainList)


def markov_Dict(size, corpus):
    """ Creating a mokup of the histogram n state """
    stateDict = {}
    secondDict = {}
    result = []
    localCorpus = word_filter(corpus)
    for index in range(len(localCorpus)):
        wordState = localCorpus[index: index + size]  # Returns a list of words
        keyString = listToString(wordState)
        startToken = index + 1
        endToken = startToken + size
        keyState = localCorpus[startToken: endToken]
        if keyString in stateDict:
            value = stateDict.get(keyString)
            secondDictValue = secondDict.get(keyString)
            value += 1
            stateDict.update({keyString: value})

            if secondDictValue is not None:
                print("addding new keyState", keyState, keyString, "secondDictValue", secondDictValue)
                secondDictValue.append([listToString(keyState), 1])
                secondDict.update({keyString: secondDictValue})
                print(secondDict.get(keyString))
            else:
                if secondDictValue is not None:
                    valueIndex = nestedList(listToString(keyState), secondDictValue)
                    print("Version 1:", secondDictValue[valueIndex], secondDictValue[valueIndex][1])
                    secondDictValue[valueIndex][1] += 1
                    print("Version 2:", secondDictValue[valueIndex][1])
                    secondDict.update({listToString(keyState): secondDictValue})
        elif keyString not in stateDict and len(keyString.split()) == size:
            stateDict.update({keyString: 1})
            if len(keyState) == size:
                print("this is the keyString:", keyString, listToString(keyState))
                secondDict.update({keyString: [[listToString(keyState), 1]]})
    result.append(stateDict)
    result.append(secondDict)
    return result  # Sample the states


def lastIndex(list):
    return list[len(list) - 1]


def createSentence(wordAmount, corpus):
    result = markov_Dict(1, corpus)
    start = sample(result[0])
    print(result[1])
    print(start + " ", end='')
    for time in range(wordAmount):
        #  previous = [] This will be used later on so the previous statements have not  been said
        start = markov_chain_v2(start, result)
        print(lastIndex(start.split()) + " ", end='')
        if start == '.':
            start = sample(result[0])


    #  markov_chain_v2(localCorpus[])


if __name__ == "__main__":
    result = createSentence(4, "I am I like I like I know am nothing like  nothing more like like")
