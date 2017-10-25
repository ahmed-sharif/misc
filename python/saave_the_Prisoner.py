

"""


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7   8  1  2 3 4 5 6 7 8
          1 2 3 4 5 6 7 8 9 10 11 12 13 



1   2   3   4   5   6   7   8
1   2   3   4   5   6   7   8




no_of_move = M % N
position = (S - 1 + no_of_move) % N


"""


test_cases = int(raw_input().strip())
for _ in range(test_cases):
    n, m, s = raw_input().strip().split()
    n, m, s = (int(n), int(m), int(s))
    no_of_move = m % n
    position = (s - 1 + no_of_move) % n
    if position == 0:
        position = n
    print position
