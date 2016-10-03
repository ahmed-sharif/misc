# https://www.hackerrank.com/challenges/ctci-making-anagrams 


def number_needed(a, b):
    freq_a = [0 for _ in range(26)]
    ord_a = ord('a')
    for char in a:
        freq_a[ord(char) - ord_a] += 1
    for char in b:
        freq_a[ord(char) - ord_a] -= 1
    
    total = 0
    for i in range(26):
        total += abs(freq_a[i])
        
    return total
      
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

