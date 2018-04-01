def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    """

    if B in A:
        return 1
    blen = len(B)
    alen = len(A)
    string = A
    count = 1
    starting_string_len = int(blen / alen)
    if (starting_string_len == 0):
        #string = A
        pass
    else:
        #string = A * starting_string_len
        count = starting_string_len
    import pdb;pdb.set_trace()
    while len(string*count) <= 10000:
        if B in string*count:
            return count
        else:
            count = count + 1
    return -1

ret = repeatedStringMatch('abcd', 'cdabcdab')
print("Output")
print(ret)