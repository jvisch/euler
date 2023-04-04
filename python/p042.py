def words():
    with open("p042_words.txt") as f:
        all_words = f.read()
    for w in all_words.split(','):
        yield w[1:-1]


def character_value(c):
    return ord(c.upper()) - ord('A') + 1


def word_value(word):
    values = (character_value(c) for c in word)
    return sum(values)


def triangle_number():
    n = 1
    while True:
        yield (n * (n+1)) // 2
        n += 1


def take_while(sequence, predicate):
    value = next(sequence)
    while predicate(value):
        yield value
        value = next(sequence)


if __name__ == '__main__':
    # get all values from the words
    word_values = [(w, word_value(w)) for w in words()]
    # get all triangle numbers
    max_value = max(v for w, v in word_values)
    triangle_numbers = take_while(triangle_number(), lambda x: x < max_value)
    triangle_numbers = list(triangle_numbers)
    # all triangle words
    triangle_words = ((w, v) for w, v in word_values if v in triangle_numbers)
    triangle_words = list(triangle_words)
    print(len(triangle_words))
