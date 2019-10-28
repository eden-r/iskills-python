def pigLatinTranslator(word):
    vowels = "aeiouAEIOU"
    word = str(word)
    if word.isdigit():
        print ("Please submit a word.")
    elif len(word) < 1:
        print ("Please submit a longer word.")
    else:
        if word[0] in vowels:
            return word + "yay"
        for letter in word:
            word = word[1:] + word[0]
            if word[0] in vowels:
                return word + "ay"
        return word[1:] + word[0] + "ay" 


wordsToTranslate = ['example', 'school', 'question', 'fig',  'answer', 'computer', 'eliminate', 'shred', 'why']

for englishWord in wordsToTranslate:
    pigLatinWord = pigLatinTranslator(englishWord)
    print("\"{}\" becomes \"{}\"".format(englishWord.capitalize(), pigLatinWord))

