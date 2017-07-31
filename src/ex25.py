def break_words(stuff):
    """This funcion will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word afterr popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sen):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sen)
    return sort_words(words)

def print_first_and_last(sen):
    """Prints the first and the last word of a sentence."""
    words = break_words(sen)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sen):
    """Sorts the words and then print first and the last word."""
    words = sort_sentence(sen)
    print_first_word(words)
    print_last_word(words)

