from time import sleep
from threading import Thread
class worker(Thread):
    def __init__(self, tasks):
        super(worker, self).__init__()
        self.tasks = tasks
        self.daemon = True
        #self.start()
    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            func(*args, **kargs)
            self.tasks.task_done()
            sleep(0)