from count_syllables import countSyllables


# main function takes input of a phrase and returns if phrase is Haiku
# if True, returns full Haiku (else blank value returned)
# sentence == full phrase input
def checkHaiku(sentence):
    # inner function will check each line in 5-7-5 format to see if it has the
    # right number of syllables and no words are broken between lines
    # sentenceList == sentence broken into list
    # maxSyllables == 5 or 7 depending on line number
    # pos == starting position for index
    def checkSentence(sentenceList, maxSyllables, pos):

        # variable to count number of syllables in each section/line
        sentenceSyllables = 0

        while True:
            # breaks if index is outside of length of list
            if pos > len(sentenceList) - 1:
                break

            # counts syllable in each word and adds to sentenceSyllables
            # until max is reached
            wordSyllables = int(countSyllables(sentenceList[pos]))

            # breaks when the number of syllables exceeds max
            if sentenceSyllables + wordSyllables > maxSyllables:
                break
            # if number of syllables is less than max, keep adding
            else:
                sentenceSyllables += wordSyllables
                pos += 1
        # will return false if the number of syllables in the section is not == max
        # this prevents false positives if half a word contributes to the max
        if sentenceSyllables == maxSyllables:
            goodLine = True
        else:
            goodLine = False

        # goodLine = boolean if line meets rules
        # pos = integer for the index where the function left off
        return goodLine, pos

    # ----------
    # split into list with words
    wordList = sentence.split()

    # posX represents index position in the list
    pos0 = 0

    # checks for first line in Haiku
    firstSentence, pos1 = checkSentence(wordList, 5, pos0)

    # counts total syllables in sentence
    # has to count list instead of sentence to avoid miscount of spaces
    totalSyllables = 0
    for word in wordList:
        totalSyllables += int(countSyllables(word))

    # conditions for isHaiku = true:
    # total syllables is 17
    # 5-7-5 structure with no word breakage
    if totalSyllables == 17:
        if firstSentence:
            secondSentence, pos2 = checkSentence(wordList, 7, pos1)
            if secondSentence:
                thirdSentence, pos3 = checkSentence(wordList, 5, pos2)
                if thirdSentence:
                    isHaiku = True
                else:
                    isHaiku = False
            else:
                isHaiku = False
        else:
            isHaiku = False
    else:
        isHaiku = False

    # combine words from list to reformat to Haiku
    if isHaiku:
        line1 = (" ".join(wordList[pos0:pos1]))
        line2 = (" ".join(wordList[pos1:pos2]))
        line3 = (" ".join(wordList[pos2:pos3]))

        haiku = (line1 + '\n' + line2 + '\n' + line3)
    else:
        haiku = ""

    return isHaiku, haiku


# Main
#while True:
#    userHaiku = input("enter your sentence: ")
#    # userHaiku = "an old silent pond a frog jumps into the pond splash silence again"
#    isHaiku, haiku = checkHaiku(userHaiku)
#    if isHaiku:
#        print("This is a Haiku!")
#        print()
#        print(haiku)
#        print()
#    else:
#        print("This is not a Haiku :( try again!")
#
## an old silent pond a frog jumps into the pond splash silence again


# add text on a random image
