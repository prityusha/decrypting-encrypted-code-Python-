def decryptLetter(letter, shiftamount):
    letterAsciiCode = ord(letter.lower())
    Ascii = ord('a')
    alphabetsize = 26
    decodeLetter = Ascii+((letterAsciiCode-Ascii)+shiftamount)%alphabetsize
    decodedLetter = chr(decodeLetter)
    return decodedLetter


def decryptWord(word, shiftamount):
    decodedword = ""
    for l in word:
        if(l==" "):
            decodedword = decodedword + " "
        else:
            Letter = decryptLetter(l,shiftamount)
            decodedword = decodedword + Letter
    return decodedword


aWord = input("Insert Encrypted Text: ")
shiftValue = int(input("Insert shift value(shift value is by how many letters is your text shifted): "))

print (f"shifting {aWord} by {shiftValue} gives: {decryptWord(aWord, shiftValue)}")