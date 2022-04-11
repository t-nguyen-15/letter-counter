def main():
    print("This program counts the number of given letters in an input phrase")
    letterToCount = input("Enter the letters to count in the phrase (e.g., 'aeiou': ").lower()
    inputPhrase = input("Enter your phrase: ").lower()

    totalOccurrencesOfLettersToTcount = 0
    for character in inputPhrase:
        if character in letterToCount:
            totalOccurrencesOfLettersToTcount += 1

    print("Total occurrences of '{}' in your phrase: {}".format(letterToCount, totalOccurrencesOfLettersToTcount))

if __name__ == "__main__":
    main()
