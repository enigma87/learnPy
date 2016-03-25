
def make_word_dict():
    """Reads the words in words.txt and returns a dictionary
    that contains the words as keys."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

#word_dict = make_word_dict()

def reduce_by_one_list(word):
    word_list = []
    for i in range(len(word)):
        word_list.append(word[0:i] + word[i+1:len(word)])
    return word_list

def filter_by_words(list_words, word_dict):
    filter_words = list()
    for word in list_words:
        if word in word_dict:
            filter_words.append(word)
    return filter_words

memoize_reducible = dict()
memoize_reducible[ '' ] = [ '' ]

def is_reducible(word, word_dict):
    reduce_by_one = list()
    reducible = list()

    if memoize_reducible.get(word,False):
        return memoize_reducible[word]

    ''' just explicitly writing out the base case '''
    if word == '':
        return memoize_reducible[ '' ]

    ''' query memoized results '''
    if memoize_reducible.get(word, False):
        return memoize_reducible[word]

    reduce_by_one = reduce_by_one_list(word)
    reduce_by_one = filter_by_words(reduce_by_one, word_dict)

    for child_word in reduce_by_one:
        child_reduce = is_reducible(child_word, word_dict)
        if child_reduce:
            #print  child_reduce
            reducible.append(child_word)

    memoize_reducible[word] = reducible
    return reducible

#f.seek(0)

#reduce_by_one = reduce_by_one_list("worshiper")
#print reduce_by_one
#print filter_by_words(reduce_by_one)

f = open("words.txt")
i = 0
for w in f:
    if is_reducible(w, make_word_dict()):
        i+=1

print i , " words"
'''
d = dict()

for word in f:
    word = word.strip()
    t = tuple(sorted(word))
    d[t] = d.get(t, [])
    d[t].append(word)
    l = d.get(t)

size_d =  dict()

for k in d.keys():
    size_d[ (len(d[k]),) +  k] = d[k]

for k in sorted(size_d.keys(), reverse=True):
    print k, size_d[k]
    if 3 == k[0]:
        break
'''
