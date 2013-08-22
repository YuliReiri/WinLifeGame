
from game.worker import worker
from Queue import Queue
class threads_pool:
    def __init__(self, threads_count):
        self.tasks = Queue(threads_count)
        for _ in range(threads_count): worker(self.tasks).start()
    
    # add task to the queue 
    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))
        
    #Wait for completion of all the tasks in the queue
    def wait_completion(self):
        self.tasks.join()