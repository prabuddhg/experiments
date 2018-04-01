# Karatsuba multiplication
from math import ceil, floor


def karatsuba(x, y):
    # base case
    if x < 10 and y < 10:  # in other words, if x and y are single digits
        return x * y
    if len(str(x)) > len(str(y)):
        y = str(y).rjust(len(str(x)),'0')
    elif len(str(y)) > len(str(x)):
        x = str(x).rjust(len(str(y)),'0')

    n = max(len(str(x)), len(str(y)))
    m = int(ceil(float(n) / 2))  # Cast n into a float because n might lie outside the representable range of integers.

    x_H = int(floor(int(x) / 10 ** m))
    x_L = int(int(x) % (10 ** m))

    y_H = int(floor(int(y) / 10 ** m))
    y_L = int(int(y) % (10 ** m))

    # recursive steps
    a = karatsuba(x_H, y_H)
    d = karatsuba(x_L, y_L)
    e = karatsuba(x_H + x_L, y_H + y_L) - a - d

    return int(a * (10 ** (m * 2)) + e * (10 ** m) + d)

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627

#a = 12345
#b = 98765
ans = karatsuba(a,b)
print ("karatsuba:%s" %ans)
check = a*b
print ("Normal:%s" %check)

diff = ans - check
print ("Diff:%s" %diff)
assert ans == check










# right_x = x%10
# left_x = int((x-right_x)/10)
# right_y = y%10
# left_y = int((y-right_y)/10)
#(left_x,right_x) = split_number(2555)
#print(left_x, " ",right_x)