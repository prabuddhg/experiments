import collections
def kEmptySlots(flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        # If the list is sorted, return -1
        # if flowers is empty, return -1
        # if k=0, return -1
        # [43 23 56 2 19 4 1 7]
        # on day 1 --> 43 place will bloom
        # on day 2 --> 23 place will bloom
        # on day 3 --> 56 place will bloom
        # on day 4 -->  2 place will bloom
        # on day 5 --> 19 place will bloom
        # on day 6 -->  4 place will bloom
        # on day 7 -->  1 place will bloom
        # on day 8 -->  7 place will bloom
        # if k=1, 41/23 means 19k not blooming
        #         23/25 means 1k not blooming between them
        # Flower [1] on [7] day
        # Flower [2] on [4] day
        # Flower [4] on [6] day
        # Flower [7] on [8] day
        # Flower [19] on [5] day
        # Flower [23] on [2] day
        # Flower [43] on [1] day
        # Flower [56] on [3] day
        # Make flower as a dict
        # now if K = 1, that means
        hash = {}
        count = 1
        for i in flowers:
            hash[int(i)] = count
            count = count + 1
        print(hash)
        arr_a = list(hash.keys())
        arr_a.sort()
        ret = None
        #for key in arr_a:
        for x in hash.keys():
            #import pdb;pdb.set_trace()
            to_find = x + int(k) + 1;
            if to_find in hash:
                day = hash[to_find]
                import pdb;pdb.set_trace()
                arr_b = list(range(x+1,to_find))
                for y in arr_b:
                    if y in hash:
                        import pdb;pdb.set_trace()
                        if hash[y] > hash[to_find]:
                            ret = day
                        else:
                            ret = -1
                            break
                if(ret == -1):
                    continue
                else:
                    return ret
            else:
                ret = -1
        return ret



#out = kEmptySlots(['43', '23', '56', '2' ,'19', '4', '1', '7'], '1')
#out = kEmptySlots(['1', '2', '3'], '1')
#out = kEmptySlots(['1', '3', '2'], '1')
#out = kEmptySlots(['1', '2', '3', '4', '5', '7', '6'], '1')
out = kEmptySlots(['6','5','8','9','7','1','10','2','3','4'],'2')
print(out)