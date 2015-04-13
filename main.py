__author__ = 'VerDe'
'''
Rules:
Words that begin with consonant the initial consonant or cluster is moved to the end of the word and "ay" is added
For words which begin with vowel sounds or silent letter, one just adds "way" (or "wa") to the end
'''

vowel_list = ["a", "e", "i", "o", "u"]

s1 = input("Throw me a word: ").lower()
start_index = len(s1)
pig_translation = ""

'''
Check if a letter is a consonant. If it is, we temporarily add it to pig_translation
If it actually is a vowel, we check if the index of the letter in our string is 0. If the word actually starts
with a vowel, different rules apply.
If it's a vowel, but it's not in the first index, there must be no more consonants at the beginning of the word
so we can apply the translation rules
'''

done = False
while done is False:
    for letter in s1:
        if letter not in vowel_list:
            pig_translation += letter
        elif s1.index(letter) == 0:
            pig_translation = s1 + "way"
            done = True
            break
        else:
            start_index = s1.index(letter)
            pig_translation = s1[start_index:] + pig_translation + "ay"
            done = True
            break

print("{0} translated to Pig Latin is {1}".format(s1, pig_translation))