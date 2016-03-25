def revprint(string):
    index = -1
    while(-len(string) <= index):
        print string[index]
        index -= 1

#revprint('bazinga')


'''
prefixes = 'JKLMNOPQ'
uprefixes ='OQ'

for a in prefixes:
    word = ''
    for b in uprefixes:
        if a == b:
            word = 'u'
    word = a + word + 'ack'
    print word
'''


def find (word, letter, index):
    while index < len(word):
        if letter == word[index]:
            return index
        index += 1
    return -1
        #print index

#print find('malayalam', 'm', 1)



def count(word, letter):
    count = 0
    indx = 0
    while True:
        indx = find(word, letter, indx)
        if (-1 == indx):
            return count
        else:
            indx += 1
            count += 1

#print count('malayalam', 'm')


def has_no_letters(s1, letterstring):
    for l in letterstring:
        if l in s1:
            return False
    return True




file = open("words.txt")
'''
#line = file.readline();
count = 0.0;
e_count = 0.0;
for line in file:
    count += 1;
    if (has_no_letters(line, "aeiou")):
        print line.strip()
        e_count += 1
    line = file.readline()
print "\% is ", (e_count/count)*100
'''
'''
def consec3(s1):
    i = 0;
    count = 0;
    while (i+1 < len(s1)):
        if s1[i] == s1[i+1]:
            count += 1;
            i = i+2
            if (3 == count):
                return True;
        else:
            count = 0;
            i = i +1
    return False

for line in file:
    word = line.strip()
    #print word,len(word)
    if (consec3(word)):
        print line.strip();
'''


def accumulator(list l):
    total = 0
    for el in l:
        if type(el) is list:
            total += sum(el)
        elif type(el) is str:
            pass
        else:
            total += int(el)
    return total



accumulator([[1,2,3],[4,5]])
