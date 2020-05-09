import re
import itertools

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']

def findAll(words, chars, jokers=1, mustInclude=None, nth=None, nthLast=None):
    allWords = []
    cartProd = list(itertools.product(alphabet, repeat=jokers))
    # all possible unique joker letter combinations
    jokerTuples = list(set([tuple(sorted(t)) for t in cartProd]))
    for p in jokerTuples:
        currentChars = chars.copy()
        currentChars.extend(p)
        reString = '^(' + '|'.join(currentChars) + '){,' + str(len(currentChars)) + '}$'
        possible = [w for w in words if re.match(reString, w)]
        for w in possible.copy():
            available = currentChars.copy()
            rejected = False
            for c in w:
                if not rejected:
                    try:
                        available.remove(c)
                    except ValueError:
                        rejected = True
                        possible.remove(w)
        allWords.extend(possible)
    if mustInclude != None:
        allWords = [w for w in allWords if all(c in w for c in mustInclude)]
    if nth != None:
        allWords = [w for w in allWords if w[nth[0]] == nth[1]]
    if nthLast != None:
        allWords = [w for w in allWords if w[-nthLast[0]] == nthLast[1]]
    return list(set(allWords))

def findAllThatContain(words, chars):
    return [w for w in words if all(c in w for c in chars)]