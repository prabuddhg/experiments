from threading import Thread
import time
import random


class ConsumerThread(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self._queue = queue

    def run(self):
        while self._queue.get(): 
            num = self._queue.get()
            self._queue.task_done()
            print("Consumed", num)
            #time.sleep(random.random())
