import re

def findAll(words, chars, mustInclude=None, nth=None, nthLast=None):
    reString = '^(' + '|'.join(chars) + '){,' + str(len(chars)) + '}$'
    possible = [w for w in words if re.match(reString, w)]
    for w in possible.copy():
        available = chars.copy()
        rejected = False
        for c in w:
            if not rejected:
                try:
                    available.remove(c)
                except ValueError:
                    rejected = True
                    possible.remove(w)
    if mustInclude != None:
        possible = [w for w in possible if all(c in w for c in mustInclude)]
    if nth != None:
        possible = [w for w in possible if w[nth[0]] == nth[1]]
    if nthLast != None:
        possible = [w for w in possible if w[-nthLast[0]] == nthLast[1]]
    return possible

def findAllThatContain(words, chars):
    return [w for w in words if all(c in w for c in chars)]