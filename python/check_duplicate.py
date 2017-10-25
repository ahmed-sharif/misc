from collections import defaultdict
store = defaultdict(list)
with open("passwd") as fd:
  for line in fd:
    parts = line.split(':')
    userid = parts[2]
    username = parts[0]
    store[userid].append(username)

for u,ii in store.iteritems():
  # print (u,i)
  i = list(ii)
  if len(i) > 1:
    print '%s:%s' % (u, ','.join(i))
