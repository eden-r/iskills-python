def pigLatinTranslator(word):
    """
    This function takes a word as its input and returns a version of the word
    translated into Pig Latin. It does not work on words that contain numbers 
    or are only one character long.
    """

    vowels = "aeiouAEIOU"
    word = str(word)
    if not word.isalpha():
        return "Please submit a single word."
    elif len(word) < 2:
        return "Please submit a longer word."
    else:
        if word[0] in vowels:
            return word + "yay"
        for letter in word:
            word = word[1:] + word[0]
            if word[0] in vowels:
                return word + "ay"
        return word[1:] + word[0] + "ay" 


wordsToTranslate = ['example', 'school', 'question', 'fig', 'answer', 'computer', 'examine', 'shred', 'why', 'a word', 'the', 'I', 24601]

for englishWord in wordsToTranslate:
    pigLatinWord = pigLatinTranslator(englishWord)
    print("Input Word: \"{}\" \t Returns: \"{}\"".format(englishWord, pigLatinWord))

