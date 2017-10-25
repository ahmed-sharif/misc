


def compress(src):
    prev = ''
    count = 1
    for ch in src:
        if ch == prev:
            count += 1
        else:
            if prev:
                print "{0}{1}".format(prev, count),
            prev = ch
            count = 1
    
    print "{0}{1}".format(src[-1], count)
        



compress('aabcccccaaa')
compress('aaaa')
compress('aaba')
compress('abba')
