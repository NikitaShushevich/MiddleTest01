def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('. ') + text.split('! ') + text.split('? ') + text.split('... ')
    return len(sentences)

def count_words_and_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        num_words = count_words(text)
        num_sentences = count_sentences(text)
        return num_words, num_sentences

# output
num_words, num_sentences = count_words_and_sentences('practice1.txt')
print('Number of words:', num_words)
print('Number of sentences:', num_sentences)
