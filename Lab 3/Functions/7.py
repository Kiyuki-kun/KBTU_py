def word_frequency(text):
    normalized_text = ''.join(e for e in text if e.isalnum() or e.isspace()).lower()
    words = normalized_text.split()
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    return word_frequencies

text = input("Enter a Sentence: ")
print(word_frequency(text))