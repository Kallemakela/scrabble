def removeDuplicateWords(path):
    fin = open(path, 'r')
    intext = fin.read()

    print('Words before')
    print(len(list(intext.split(','))))
    print('Unique words before')
    print(len(list(set(intext.split(',')))))

    out = ','.join(list(set(intext.split(','))))

    print('Words after')
    print(len(list(out.split(','))))
    print('Unique words after')
    print(len(list(set(out.split(',')))))

    fout = open(path, 'w')
    fout.write(out)

def removeWord(path, word):
    fin = open(path, 'r')
    intext = fin.read()

    print('Words before')
    print(len(list(intext.split(','))))
    print('Unique words before')
    print(len(list(set(intext.split(',')))))

    out = intext.replace(',' + word + ',', ',')

    print('Words after')
    print(len(list(out.split(','))))
    print('Unique words after')
    print(len(list(set(out.split(',')))))

    fout = open(path, 'w')
    fout.write(out)