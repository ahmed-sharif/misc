


a = [2,  2,  3,  5,  5,  7,  11, 11, 11, 13] 


print a[0],
last = a[0]
last_index = 0
for i in range(1, len(a)):
    if a[i] == last:
        pass
    else:
        last = a[i]
        print a[i],
        a[last_index+1] = a[i]
        last_index += 1

print


print a[:last_index+1]
