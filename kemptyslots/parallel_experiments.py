from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time

tasks = [
  'TASK-1',
  'TASK-2',
  'TASK-3',
  'TASK-4',
  'TASK-5',
  'TASK-6',
  'TASK-7',
  'TASK-8',
  'TASK-9',
  'TASK-10',
  'TASK-11',
  'TASK-12',
  'TASK-13',
  'TASK-14',
  'TASK-15',
  'TASK-16',
  ]

def run(task):
    print("Running %s" %task)
    if task == "TASK-5":
        result =  task + " failed"
        print("sleeping for 2 seconds")
        time.sleep(10)
        raise
    else:
        result =  task + " is done" 
    return result

#for entry in tasks:
#   run(entry)


pool = ThreadPool(4)
results = pool.imap(run, tasks)
import pdb;pdb.set_trace()
pool.close()
pool.join()
