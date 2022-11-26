def printCross():
    print('+', ' ', '–', ' ', '–',' ', '–',' ', '–', '+', ' ', '–', ' ', '–',' ', '–',' ', '–')
    print()

printCross()


def print_spam(huy):
    print(huy)

def do_twice (f,v):
    f(v)
    f(v)

do_twice(print_spam,'pizda')

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice,'spammmm')

def do_four(f,four):
    do_twice(f,four)
    do_twice(f,four)

do_four(print_spam, 'nein')

def printCross():
    print('+', ' ', '–', ' ', '–',' ', '–',' ', '–', ' ', '+', ' ', '–', ' ', '–',' ', '–',' ', '–',' ', '+')
def printCol():
    print('|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|')
def printFourCol(f):
    f()
    f()
    f()
    f()
def exThreeTwo():
    printCross()
    printFourCol(printCol)
    printCross()
    printFourCol(printCol)
    printCross()

exThreeTwo()


