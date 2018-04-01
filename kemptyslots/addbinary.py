
bit_dict = {
    '111': "1,1",
    '110': "0,1",
    '101': "0,1",
    '100': "1,0",
    '011': "0,1",
    '010': "1,0",
    '001': "1,0",
    '000': "0,0",
}

def add_binary_bit(a,b,ca):
    key = str(a) + str(b) + str(ca)
    print(key)
    return bit_dict[key]



def add_binary(A,B):
    carry = 0
    Output = []
    for i in range (0, len(A)):
        print(i, "=")
        out = add_binary_bit(A[i], B[i], carry)
        print(out)
        import pdb; pdb.set_trace()
        m = out.split(",")
        Output[i] = m[0]
        carry = m[1]
        print (Output[i], carry)
    if carry:
        Output[i+1] = carry

A = [1,1,1,1]
B = [1,1,1,1]
out = add_binary(A,B)
print(out)

