f=open('07')

for l in f:
    ll = l.split()
    ll = map(int, ll)
    print sum(ll), max(ll), len(ll)
f.close()
