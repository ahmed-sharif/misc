# https://www.hackerrank.com/challenges/coin-change

# this is not the classic coin change problem
# this is the "count the number of score of combination problem"
# how many differeny you can choose a set of coins to get a target sum

N, C = map(int, raw_input().strip().split())
coins = map(int, raw_input().strip().split())

dp_table = []
for _ in range(C):
    dp_table.append([0 for _ in range(N + 1)])

dp_table[0][0] = 1
# fill the first row
for j in range(1, N + 1):
    if j % coins[0] == 0:
        dp_table[0][j] = 1
    else:
        dp_table[0][j] = 0

# fill the rest of the row
for i in range(1, C):
    for j in range(N + 1):
        with_out_this_coin = dp_table[i - 1][j]
        if j >= coins[i]:
            with_this_coin = dp_table[i][j - coins[i]]
            dp_table[i][j] = with_out_this_coin + with_this_coin
        else:
            dp_table[i][j] = with_out_this_coin
# print dp_table
print dp_table[-1][-1]            



