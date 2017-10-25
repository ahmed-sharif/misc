

def determine_minimum(lps):
	n = len(lps)
	last_index = n - 1
	last_val = lps[last_index]
	diff = n - last_val
	found = False

	res = -1
	while True:
		last_index = last_index - diff
		if lps[last_index] == 0 and last_index == diff - 1:
			found = True
			res = diff
			break
		if last_index < 0:
			break
	return res	

def compute_longest_prefix_suffix(pattern):
    
	lps = [0 for x in range(len(pattern))]
	index = 0 
	n = len(pattern)
	i = 1
	while i < n:
		if pattern[i] == pattern[index]:
			lps[i] = index + 1
			index += 1
			i += 1
		else:
			if index != 0:
				index = lps[index - 1]
			else:
				lps[i] = 0
				i += 1
	return lps

s = raw_input().strip()
m = int(raw_input().strip())
lngth = len(s)
res = m / lngth
if lngth == 1:
	res = m / lngth
else:
	lps = compute_longest_prefix_suffix(s)
	last_val = lps[-1]

	if last_val != 0:
		r = determine_minimum(lps)
		if r != -1:
			res = m / r
	


print res % 1000000007
