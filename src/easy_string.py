# given a corpus, return a dictionary with word count
def word_count(corpus = ""):
    # Low case everything initially
    mod_corpus = corpus.lower()
    # SPlit corpus into words
    words = mod_corpus.split()
    # Initialize word count dictionary
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 

    return word_count
    

# remove all concurrencies of word in a given text
def remove_word(corpus = "", word = ""):
    pass
