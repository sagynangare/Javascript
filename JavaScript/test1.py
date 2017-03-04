"""To Map A -> D, m ->p likewise
    String is string parameter
    String parameter can be string or para or word
"""
import string1
def String_Amaze(String):
    NewString = ' '
    for word in String:
        if word == ' ':
            Ascii = ord(word)
        else:
            for pun in string1.punctuation:
                if word == pun:
                    Ascii = ord(word)
                    break
                Ascii = (ord(word) - 3)
                if word.isnumeric():
                    Ascii = ord(word)
                    if word.isalpha():
                        if ((word.isupper() and Ascii > 90) or (word.islower() and Ascii > 122)):
                            Ascii = Ascii - 26
                            if ((word.isupper() and Ascii < 65) or (word.islower() and Ascii < 97)):
                                Ascii = Ascii + 26
                                NewString = NewString + chr(Ascii)
                                print ("Output=> \n", NewString)
                                
String = raw_input('Enter the String = ')
String_Amaze(String)
