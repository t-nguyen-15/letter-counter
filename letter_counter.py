def getInputPhrase():
    return input("Enter your phrase: ").lower()

def getTotalOccurrencesOfLettersToTcount(phrase, letterToCount):
    totalOccurrences = 0
    for character in phrase:
        if character in letterToCount:
            totalOccurrences += 1
    
    return totalOccurrences

def main():

    print("This program counts the number of given letters in an input phrase")
    letterToCount = input("Enter the letters to count in the phrase (e.g., 'aeiou': ").lower()
    inputPhrase = getInputPhrase()

    totalOccurrencesOfLettersToTcount = getTotalOccurrencesOfLettersToTcount(inputPhrase, letterToCount)

    print("Total occurrences of '{}' in your phrase: {}".format(letterToCount, totalOccurrencesOfLettersToTcount))

if __name__ == "__main__":
    main()
