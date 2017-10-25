
from copy import copy

choices = [5, 3, 2]

def traverse(items, n=0):
    raw_input()
    print items, n
    citems = copy(items)
    for i in xrange(len(citems)):
        for c in choices:
            if citems[i] % c == 0:

                total = citems[i] / c
                citems[i] = total

                for x in xrange(1, c):
                    citems.append(total)

                traverse(citems, n + 1)







traverse([15])

