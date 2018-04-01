#!/usr/bin/env python3

def output():
    #return "hello world"
    a = 'aaa'
    i = 20
    while i > 0:
        a = a + a
        i = i - 1
    return a

out = output()
print(out)
