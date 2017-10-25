from copy import deepcopy, copy

class Solution(object):
    def fourSum(self, S, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # S = [1, 0, -1, 0, -2, 2]


        print S
        print
        store = {}
        for i in xrange(len(S) - 1):
            for j in xrange(i+1, len(S)):
                # print S[i],S[j]
                target = S[i] + S[j]
                if target in store:
                    # store[target].append([S[i],S[j]])
                    store[target].append([i,j])
                else:
                    # store[target] = [[S[i],S[j]]]
                    store[target] = [[i,j]]

        # target = 4
        # target = 0

        
        final_result = set()
        for k, v in store.iteritems():
            # print k, v
            needed = target - k
            if needed in store:
                if needed == k:
                    total_candidate = len(v)
                    if total_candidate > 1:
                        for i in xrange(total_candidate - 1):
                            for j in xrange(i + 1, total_candidate):
                                temp = copy(v[i])
                                temp.extend(v[j])
                                if len(set(temp)) == 4:
                                    print "t",v[i],v[j]
                                    print temp
                                    final_result.add(tuple(sorted(temp)))

                else:
                    for val in v:
                        for val2 in store[needed]:
                            temp = copy(val)
                            temp.extend(val2)
                            if len(set(temp)) == 4:
                                print 't', val, val2
                                print temp
                                final_result.add(tuple(sorted(temp)))


        def get_original_items(tpl):
            res = [S[index] for index in tpl]
            return res

        
        return [get_original_items(item) for item in final_result]




