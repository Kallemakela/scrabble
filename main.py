from find import findAll, findAllThatContain
from points import sortByPoints
from wordManager import removeDuplicateWords, removeWord

path = 'data/words.txt'

f = open(path, "r")
allWords = list(set(f.read().split(',')))
f.close()
# only using words that are shorter than 9 chars
words = [w for w in allWords if len(w) <= 9]

initInput = input(
    '''\n
    0: find all words for given characters\n
    1: find all words that contain given characters\n
    2: remove given word\n
    3: remove duplicate words\n\n
    '''
    )
cmd = 0 if initInput == '' else int(initInput)

if cmd == 0:
    chars = list(input('Type characters\n'))

    mustIncludeInput = input('Must include chars\n')
    mustInclude = None if mustIncludeInput == '' else list(mustIncludeInput)

    nthInput = input('Nth letter in form: n letter. 0 is the first letter.\n')
    nth= None if nthInput == '' else (int(nthInput.split(' ')[0]), nthInput.split(' ')[1])

    nthLastInput = input('Nth last letter in form: n letter. 1 is the first letter.\n')
    nthLast = None if nthLastInput == '' else (int(nthLastInput.split(' ')[0]), nthLastInput.split(' ')[1])

    jokersInput = input('# of jokers. Default 1.\n')
    jokers = 1 if jokersInput == '' else int(jokersInput)

    print('\nSearching...\n')
    sorted = sortByPoints(findAll(words, chars, jokers=jokers, mustInclude=mustInclude, nth=nth, nthLast=nthLast))
    for p in sorted:
        print(p[0] + ' ' + str(p[1]))
elif cmd == 1:
    chars = list(input('Type characters\n'))
    print(findAllThatContain(words, chars))
elif cmd == 2:
    word = input('Word\n')
    removeWord(path, word)
elif cmd == 3:
    removeDuplicateWords(path)
else:
    print("Unknown command")

# TODO support empty chars (jokers)