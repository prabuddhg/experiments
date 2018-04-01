def insertion_sort(A):
    for j in range(1, len(A)):
        #import pdb;pdb.set_trace()
        key = A[j]
        i = j - 1
        print("key:", key, " j: ", j, " i: ", i)

        print (i, " >= 0 and ", A[i], " > ", key)
        while i >= 0 and A[i] > key:
            print("Inside while ", i, " >= 0 and ", A[i], " > ", key)
            A[i+1] = A[i]
            i = i -1
            print ("new A in while", A)
            print("i=", i)
        A[i+1] = key
        print("new A outside while==========", A)
    return A

def insertion_sort_reverse(A):
    for j in range(1, len(A)):
        #import pdb;pdb.set_trace()
        key = A[j]
        i = j - 1
        print("key:", key, " j: ", j, " i: ", i)

        print (i, " >= 0 and ", A[i], " < ", key)
        while i >= 0 and A[i] < key:
            print("Inside while ", i, " >= 0 and ", A[i], " > ", key)
            A[i+1] = A[i]
            i = i -1
            print ("new A in while", A)
            print("i=", i)
        A[i+1] = key
        print("new A outside while==========", A)
    return A

#new_A = insertion_sort_reverse([5,2,4,6,1])
new_A = insertion_sort_reverse([31,41,59,26,41,58])

print(new_A)