import lib.producer as producer
import lib.consumer as consumer
from Queue import Queue
import time

print("Start process")
t0 = time.time()


queue = Queue(10)
producer_obj = producer.ProducerThread(queue)
producer_obj.start()
producer_obj.join()

workers = []
size = producer_obj.size()
for _ in range(size):
     worker = consumer.ConsumerThread(queue)
     worker.start()
     workers.append(worker)

for worker in worker_threads:
     worker.join()


t1 = time.time()
total = t1-t0
print("Done in %s seconds", total)
