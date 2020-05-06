points = {
    'a': 1,
    'b': 8,
    'c': 10,
    'd': 7,
    'e': 1,
    'f': 8,
    'g': 8,
    'h': 4,
    'i': 1,
    'j': 4,
    'k': 2,
    'l': 2,
    'm': 3,
    'n': 1,
    'o': 2,
    'p': 4,
    'q': 0,
    'r': 4,
    's': 1,
    't': 1,
    'u': 3,
    'v': 4,
    'w': 7,
    'x': 0,
    'y': 4,
    'z': 0,
    'å': 0,
    'ä': 2,
    'ö': 7
}

def countPoints(word):
    p = 0
    for c in word:
        p += points[c]
    # all letters used bonus
    p += 50 if len(word) == 8 else 0
    return p

def sortByPoints(words):
    wordPointPairs = [(w, countPoints(w)) for w in words]
    return sorted(wordPointPairs, key=lambda p: p[1])