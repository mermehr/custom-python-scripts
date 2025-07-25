# Coverts english to pig latin
print('Enter the English message to translate into pig latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in pig Latin
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetter = ''
    while len(word) > 0 and not word[0]:
        prefixNonLetter += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetter)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1] + suffixNonLetters
        word = word[:-1]

    # Remember if the word was in uppercase or title case:
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation

    # Separate the constants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the pig latin ending to words:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word
    pigLatin.append(prefixNonLetter + word + suffixNonLetters)

# Join all the words back together into a single string
print(' '.join(pigLatin))
