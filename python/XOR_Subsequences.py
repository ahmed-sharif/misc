n = int(raw_input().strip())

numbers = [0 for _ in range(n)]

for i in range(n-1,-1,-1):
    num = int(raw_input().strip())
    numbers[i] = num
    
