# https://www.hackerrank.com/challenges/ctci-array-left-rotation
def array_left_rotation(a, n, k):
    k = k % n
    # reverse first k elements
    for i in range(k/2):
        a[i], a[k-1-i] = a[k-1-i], a[i]

    # reverse items k to n
    for i in range(k, k + (n-k)/2): 
        a[i], a[n - 1 - i + k] = a[n - 1 - i + k], a[i]

    # reverse the whole list again
    for i in range(n/2):
        a[i], a[n-1-i] = a[n-1-i],  a[i]
  

n, k = map(int, raw_input().strip().split())
a = map(int, raw_input().strip().split())
array_left_rotation(a, n, k);
print ' '.join(map(str,a))

