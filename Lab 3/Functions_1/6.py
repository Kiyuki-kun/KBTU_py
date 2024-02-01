def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    print(reversed_sentence)

sentence = input("Enter a sentence: ")
reverse_words(sentence)
