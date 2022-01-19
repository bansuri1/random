# Adds letter to each value at end of list and converts to tuple

import sys


def countSyllables(word):
    # appends plural and past tense
    # create sep function for this eventually with other things like -ies and exceptions for global exceptions dict
    def appendMergeSuffix(list):
        masterList = []
        eEnding = ('s', 'x', 'sh', 'ch', 'z')
        for word in list:
            masterList.append(word)
            if word.endswith('e'):
                plural = word + 's'
                past = word + 'd'
            elif word.endswith(eEnding):
                plural = word + 'es'
                past = word + 'ed'
            else:
                plural = word + 's'
                past = word + 'ed'
            # wordList = [word, plural, past]
            masterList.append(past)
            masterList.append(plural)
        return tuple(masterList)

    # vowels list
    vowels = 'aeiouy'
    twoSyllable = ['ao', 'eo', 'ia', 'io', 'iu', 'oe', 'ua', 'ue', 'ui', 'uo']

    suffix1 = ['s', 'd']
    suffix2 = ['s', 'ed']
    # all endings with 2 or more vowels to be counted as one syllable

    oneSyllableEnding = ('tian', 'tion', 'cian', 'cion', 'sian', 'sion')
    oneSyllableEnding = appendMergeSuffix(oneSyllableEnding)

    # -e endings to count as 2 syllables
    eEndings2 = ('ble', 'dle', 'cle', 'ple', 'bole', 'gle')
    eEndings2 = appendMergeSuffix(eEndings2)

    # -e endings to count as 0 syllables
    eEndings0 = ('gue', 'que')
    eEndings0 = appendMergeSuffix(eEndings0)

    plEndings1 = ('ses', 'ches', 'shes', 'xes', 'zes', 'ies')
    pastEndings1 = ('ied')

    # add plurals
    globalExceptions = {'rhythm': 2,
                        'simile': 3,
                        'business': 2,
                        'someone': 2,
                        'sour': 2,
                        'hour': 2,
                        'our': 2,
                        'oil': 2,
                        'coincidence': 4,
                        'ukulele': 4,
                        'argue': 2,
                        'ague': 2,
                        'segue': 2,
                        'she': 1,
                        'tried': 1,  # will not work with function
                        'tries': 1  # will not work with function
                        }
    word = word.lower()

    #specialChar = ["\'", '.', ',', '/', '!', '@', '#', '-', '~', '$', '%', '^', '&', '*', '(', ')', '+', '=', '[', ']',
            #       '{', '}', '?', ':', ';']
   # for char in specialChar:
       # word = word.replace(char, "")

    count = 0
    if word in globalExceptions.keys():
        count = globalExceptions[word]
    else:
        if word[0] in vowels:
            count += 1
            # clean up below
        for i in range(1, len(word)):
            if word[i] in vowels:
                count += 1
            if word[i] in vowels and word[i - 1] in vowels:
                if word[i - 1] + word[i] not in twoSyllable:
                    count -= 1
            if word[i] in vowels and word[i - 1] == 'q':
                count -= 1

        if word.endswith('e') or word.endswith('es') or word.endswith('ed'):
            if word.endswith(eEndings2) or word.endswith(plEndings1):
                pass
            elif word.endswith(eEndings0):
                count -= 2
            elif word.endswith(plEndings1):
                pass
            else:
                count -= 1

        if word.startswith('mc'):
            count += 1
        # maybe remove
        if word.startswith('trie') or word.startswith('bie'):
            count += 1

        if word.endswith(oneSyllableEnding):
            count -= 1

        if count == 0:
            count = 1
    return str(count)

# Main
# while True:
#   word = input ('Enter a word: ')
#  if word == 'q':
#     sys.exit('Program terminated.')
# syllables = countSyllables(word)
# print('The number of syllables in ' + word + ' is ' + syllables + '.')


# add pre- co- + vowel
