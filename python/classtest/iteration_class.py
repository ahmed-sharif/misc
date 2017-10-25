


class Iclass(object):
    def __getitem__(self, i):
        return self.items[i]
    def __init__(self, items):
        self.items = items
    def __iter__(self):
        return self.items.__iter__()



i = Iclass([1,2,3,4])
print i[0]

for x in i:
    print x
