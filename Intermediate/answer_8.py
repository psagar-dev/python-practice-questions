#Write a Python program to reverse the order of words in a sentence.

def reverseWords(sentence):
    
    return ' '.join(sentence.split()[::-1])

sentence = input("Enter the world: ")

reversedSentence = reverseWords(sentence)
print("Reversed Sentence:", reversedSentence)