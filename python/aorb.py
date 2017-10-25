
"""

"B9"
"40"
"5A"

1   1   1
0   0   0
0   1   1
1   0   1



1   1   0   0   1   0   1


1   

0   0   1
0   1   0
1   0   0
1   1   0


    1 0 1 0
1 0 1 0 0 0
  1 1 0 1 0

10BA  0000  0000  0000  0000
0121  0000  1010  1111  1001
0AF9  0000  1010  1111  1001

       



1 0 0 1

1 0 0 1

1   0   1   1   1

0   0   1   0   1
1   1   0   0   1     


maxlen - minlen - 1


cp = '01011010'

ap = '00011000'
bp = '01000010'



1  1  0  0  1
0  1  0  0  0

1  1  0  1  0


0  0  0  1  1  0  0  0
0  1  0  0  0  0  1  0
"""
def get_solution(A, B, C, K):
    a_bin = list(bin(int(A, 16))[2:])
    org_a_bin = list(bin(int(A, 16))[2:])
    b_bin = list(bin(int(B, 16))[2:])
    org_b_bin = list(bin(int(B, 16))[2:])
    c_bin = list(bin(int(C, 16))[2:])
    org_c_bin = list(bin(int(C, 16))[2:])

    # print "input ", A, B, C

    max_len = max((len(a_bin), len(b_bin), len(c_bin)))

    #if len(a_bin) < max_len and len(b_bin) < max_len:
    #    print "regg"
    #    return 0, 0, -1

    if len(c_bin) < max_len:
    #    print "re"
        c_bin = (['0'] * (max_len - len(c_bin))) + c_bin

    if len(a_bin) < max_len:
        a_bin = (['0'] * (max_len - len(a_bin))) + a_bin

    if len(b_bin) < max_len:
        b_bin = (['0'] * (max_len - len(b_bin))) + b_bin

    


    min_len = min((len(a_bin), len(b_bin), len(c_bin)))

    a_lowest = max_len - len(a_bin)
    b_lowest = max_len - len(b_bin)

    #print a_bin
    #print b_bin
    #print c_bin
    #print "---------"
    alternation = 0

    for i in range(len(a_bin) - 1, - 1, -1):
        # print "hello"
        a_digit = a_bin[i]
        b_digit = b_bin[i]
        c_digit = c_bin[i]

        if(int(a_digit)|int(b_digit) != int(c_digit)):
            """
            0   0   1
            0   1   0
            1   0   0
            1   1   0
            """

            if a_digit == '0' and b_digit == '0' and c_digit == '1':
                b_bin[i] = '1'
                #if i < b_lowest:
                #    a_bin[i] = '1'
                #else:
                #    b_bin[i] = '1'
                alternation += 1
            elif a_digit == '0' and b_digit == '1' and c_digit == '0':
                b_bin[i] = '0'
                alternation += 1
            elif a_digit == '1' and b_digit == '0' and c_digit == '0':
                a_bin[i] = '0'
                alternation += 1
            elif a_digit == '1' and b_digit == '1' and c_digit == '0':
                a_bin[i] = '0'
                b_bin[i] = '0'
                alternation += 2
            
            if alternation > K:
                return a_digit, b_digit, -1
    r_a = int(''.join(a_bin),2)
    r_b = int(''.join(b_bin),2)
    r_c = int(''.join(c_bin),2)

    if(r_a|r_b != r_c):
        return a_digit, b_digit, -1

    # print "after first pass"
    # print a_bin
    # print b_bin
    # print c_bin
    # print "ends ----", alternation            

    # print "-----"            
    for i in range(len(a_bin)):
        #print a_bin, i, a_bin[i]
        a_digit = a_bin[i]
        b_digit = b_bin[i]
        c_digit = c_bin[i]

        """
        1   1   1

        1   0   1
        """
        if alternation >= K:
            break

        if(int(a_digit)|int(b_digit) == int(c_digit)):
            if a_digit == '1' and b_digit == '1' and c_digit == '1':
                a_bin[i] = '0'
                alternation += 1
            elif a_digit == '1' and b_digit == '0' and c_digit == '1':
                if alternation + 2 > K:
                    continue
                if i < b_lowest:
                    continue
                a_bin[i] = '0'
                b_bin[i] = '1'
                alternation += 2
        #print "end=", a_bin

    # print "return"            
    return a_bin, b_bin, alternation        



test_cases = int(raw_input().strip())

for _ in range(test_cases):
    k = int(raw_input().strip())
    A = raw_input().strip()
    B = raw_input().strip()
    C = raw_input().strip()
    #print A
    #print B
    #print C
    #a_bin = list(bin(int(A, 16))[2:])
    #b_bin = list(bin(int(B, 16))[2:])
    #c_bin = list(bin(int(C, 16))[2:])

    #print " ".join(a_bin)
    #print " ".join(b_bin)
    #print " ".join(c_bin)

    # print "start-------"
    ad, bd, alt = get_solution(A, B, C, k)
    # print "res -------", alt
    if alt == -1:
        print -1
    else:
        r1 = (hex(int(''.join(ad), 2))[2:]).upper()
        if r1[-1] == 'L':
            print r1[:-1]
        else:
            print r1
        r2 =  (hex(int(''.join(bd), 2))[2:]).upper()
        if r2[-1] == 'L':
            print r2[:-1]
        else:
            print r2

