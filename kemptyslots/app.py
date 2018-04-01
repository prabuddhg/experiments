#!/usr/bin/env python3

from subprocess import Popen, PIPE
import os, sys, time

cmd = os.getcwd()

cmd = cmd + '/' + "./hello.sh"
limit = 'ulimit -v 2621;'
new_cmd = limit + cmd
print(cmd)
out = open('/Users/pg/PycharmProjects/kemptyslots/out', 'r+')
err = open('/Users/pg/PycharmProjects/kemptyslots/err', 'r+')
i=10
while i > 0:
    #p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    p = Popen(cmd, stdout=out, stderr=err)
    while p.poll() == None:
        # We can do other things here while we wait
        time.sleep(.1)
        p.poll()
    import pdb;pdb.set_trace()
    (out_,err_) = p.communicate(timeout=150)

    out_ = str(i) + "=" + str(out_)
    print(i)
    out.write(out_)
    i=i-1
print ("=====Done")