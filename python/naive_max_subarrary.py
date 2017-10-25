


nums = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]


sums = [[None] * len(nums) for i in range(len(nums))]

# print len(sums)
# print len(sums[0])

count = 0

for i in range(len(sums)):
    sums[i][i] = nums[i]



mx = 0
for i in range(len(nums) - 1):
    s = nums[i]
    for j in range(i+1, len(nums)):
        #count += 1
        #s = s + nums[j]
        #s = 0
        #for k in range(i, j + 1):
        #    count += 1
        #    s += nums[k]
        #    print nums[k],
        #print
        count += 1
        sums[i][j] = sums[i][j-1] + nums[j]
        # sums[i][j] = s
        if sums[i][j] > mx:
            mx = sums[i][j]
        print "sum of {0} - {1} = {2}".format(i, j, s) 
    # sums[i][j] = s
    # print "sum of {0} - {1} = {2}".format(i, j, s) 

print "max = " + str(mx)
print count
for s in sums:
    print s






