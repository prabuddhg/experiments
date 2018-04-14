from threading import Thread
import time
import random

class ProducerThread(Thread):

    def __init__(self, queue): 
        Thread.__init__(self) 
        self._queue = queue
        self._nums = [x for x in range(0, 10)]

    def size():
        return len(self._nums)

    def run(self):
        while self._nums:
            num = random.choice(self._nums)
            self._queue.put(num)
            print("Produced", num)
            self._nums.remove(num) 
            time.sleep(random.random())
