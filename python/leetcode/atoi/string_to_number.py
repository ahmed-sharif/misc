




def sol(s):
    period_found = False

    result = 0

    current_power = -1

    for ch in s:
        if ch >= '0' and ch <= '9':
            digit = ord(ch) - ord('0')
            if period_found:
                result = result + pow(10, current_power) * digit
                current_power -= 1
            else:
                result = result * 10 + digit
        elif ch == '.':
            period_found = True
    return result



print sol('12345.987')
print sol('12345')
print sol('.12345')
