from random import randint


def randomWords(sentence, n = 5):
    sentence = sentence.replace(",","").replace(".","").replace("- ","")
    words = sentence.split(" ")
    resultSentence = ""
    # generowanie nowego losowego zdania o okreslonej liczbie slow
    for i in range(n):
        resultSentence += words[randint(0, len(words)-1)] + " "
    resultSentence = resultSentence[0:1].upper() + resultSentence[1: len(resultSentence) - 1].lower() + "."
    return resultSentence

zdanie = "wklej w cudzysłów zdanie bardzo proszę"
print(randomWords(zdanie, n = 10))