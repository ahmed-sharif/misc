import re

def find_all_pos(input, s):
    start = 0
    while True:
        pos = input.find(s, start)
	if pos == -1:
            break
        yield pos
        start = pos + 1

def generate_substr(input):
    for i in range(1, len(input) + 1):
        for j in range(len(input)-i+1):
            yield input[j:j+i]

def find_number(input, occ):
    mx = 0	
    sub_str_set = set()
    for sub_str in generate_substr(input):
        if sub_str not in sub_str_set: 
	    input_list = list(input)
            for pos in find_all_pos(input, sub_str):
                for k in range(pos, pos + len(sub_str)):
                    input_list[k] = 'X'
            result= ''.join(input_list) 
	    islands = re.findall(r'X+', result)
	    islands = [x for x in islands if x]
	    # print len(islands)
	    if len(islands) == occ:
	        mx += 1	    
		# print islands, sub_str
        sub_str_set.add(sub_str)
    return mx

def main():
    input = raw_input()
    n = raw_input()
    print find_number(input, int(n))

if __name__ == '__main__':
    main()
