
def merge_inver(arr):
    if len(arr) <= 1:
        return (arr,0)

    middle = len(arr) / 2
    (left, left_count) = merge_inver(list[:int(arr)])
    (right, right_count) = merge_inver(list[int(arr):])
    (whole, inver) = count_inver(left,right)
    return (whole, left_count+right_count+inver)

def count_inver(left, right):
    length = len(left+right)
    k = 0; i=0; j=0; inversion=0
    whole = list()
    while (k < length):
        if (left[i]<right[j]):
            whole[k] = left[i]
            i += 1; k += 1;
        elif (left[i]>right[j]):
            whole[k] = right[j]
            j += 1; k += 1;
            inversion = (len(left) - i) + inversion
    return (whole, inversion)
