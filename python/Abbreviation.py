

import copy



def num_of_upper(in_str):
    return sum(1 for x in in_str if x.isupper())

def print_res(original_str, p_str):
    #original_str = "aaaaaaAAaaaAaaAAAaa"
    # print original_str
    conv_str = original_str.upper()

    #p_str = "AAA"

    i = 0 


    mx_occ = 0
    total_match = 0
    mx_occ_index = 0
    while True:
        r = conv_str.find(p_str, i)
        if r == -1:
            break
        total_match += 1
        # print "found position", r, original_str[r:r+len(p_str)], num_of_upper(original_str[r:r+len(p_str)])
        nup = num_of_upper(original_str[r:r+len(p_str)])
        if nup > mx_occ:
            mx_occ = nup
            mx_occ_index = r
        i = r + 1

    if total_match == 0:
        start = 0
        end = len(original_str)
        matches = []
        current_match = []
        matches.append(current_match)
        xi = 0
        # print original_str, p_str
        while xi < len(p_str) and start < end:
            if original_str[start].upper() == p_str[xi]:
                xi += 1
                current_match.append(start)
                
            start += 1
            if xi == len(p_str):
                xi = 0
                current_match = []
                matches.append(current_match)

        matches = [match for match in matches if len(match) == len(p_str)]
        b_mat = copy.deepcopy(matches)        
        if matches:
            #print matches

            if len(matches) > 1:
                for m in matches:
                    for ind, c in enumerate(m):
                        m[ind] = original_str[c]

                #print matches
                f_res = [ num_of_upper(''.join(m))  for m in matches]
                ano_res = [ fr for fr in f_res if fr > 0]
                #print f_res
                #print ano_res

                if len(ano_res) > 1:
                    print "NO"
                else:
                    #print "\t", f_res,ano_res
                    for ind, xxs in enumerate(f_res):
                        if xxs > 0:
                            #print xxs, ind
                            #print b_mat[ind]
                            tmp_str = []
                            for i, sr in enumerate(original_str):
                                if i not in b_mat[ind]:
                                    tmp_str.append(sr)
                            if num_of_upper("".join(tmp_str)) > 0:
                                print "NO"
                            else:
                                print "YES"
                            break

                    #print "YES"
            else:
                # print matches
                print "YES"
        else:
            print "NO"
    else:

        # print "max", mx_occ_index, original_str[mx_occ_index:mx_occ_index+len(p_str)]
        # print original_str
        res = original_str[:mx_occ_index] + original_str[mx_occ_index+len(p_str):]
        # print original_str[:mx_occ_index] + original_str[mx_occ_index+len(p_str):]
        fres = num_of_upper(res) 
        # print num_of_upper(res)

        if fres == 0:
            print "YES"
        else:
            print "NO"


n = int(raw_input().strip())
for _ in range(n):
    org = raw_input().strip()
    patt = raw_input().strip()
    #print org, patt
    print_res(org, patt)

