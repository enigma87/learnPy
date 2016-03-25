def ack(m, n):
    if m < 0 or n < 0:
        return 0;
    if 0 == m:
        return n+1;
    elif m > 0 and 0 == n:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

#print ack(3, 5)

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1, -1]

def ispalindrome(word):
    tempword = word
    while (len(tempword) > 1):
        if (first(tempword) != last(tempword)):
            return False
        tempword=tempword[1:-1]
    return True

#if (ispalindrome('malayaalam')):
#    print "is a pal"

def ispow(power, number):
    if (number == power):
        return True
    else:
        #print "p" , power, " n", number
        return ispow(power/number, number)

#print ispow(625, 5)

def gcd (a,b):
    if (0 == a or 0 == b):
        return a or b
    c = 0;
    if (a < b):
        c = a
        d = b
    elif b < a:
        c = b
        d = a
    return gcd(c, d % c)


#print gcd(72, 32)


def NewtonRoot(num):
    x = num
    y = 0.0
    while True:
        y = x + num/x
        y = y/2.0
        if abs(x - y) < 0.00000001:
            break
        x =y
    #print y
    return y

from math import *;

for i in (1.0, 2.0,3.0,4.0, 5.0, 6.0, 7.0, 8.0, 9.0):
    a = NewtonRoot(i)
    b = sqrt(i)
    print i, "\t", a, "\t\t\t", b, "\t\t\t", abs(a-b)
