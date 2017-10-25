




def computeTemporaryArray(pattern):
	print pattern, len(pattern)
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


print computeTemporaryArray("aabaabaaa")
print computeTemporaryArray("abab")
print computeTemporaryArray("abc")
print computeTemporaryArray("ab")
print computeTemporaryArray("aa")
print computeTemporaryArray("a")
print computeTemporaryArray("abababab")
print computeTemporaryArray("abcabcabc")
print computeTemporaryArray("abcabcabcabc")
print computeTemporaryArray("abcabcsbcabc")

print computeTemporaryArray("abcdabcdabcdabcdabcd")




