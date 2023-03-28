def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('. ') + text.split('! ') + text.split('? ') + text.split('... ')
    return len(sentences)
