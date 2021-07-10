def func(word):
    if len(word) <= 10:
        return word
    else:
        wordZero = word[0]
        nums = len(word) - 2
        wordEnd = word[len(word)-1]
        new_word = f'{wordZero}{nums}{wordEnd}'
        return new_word

print(func('IAmAVeryCoolBoyThanksForAsking'))
