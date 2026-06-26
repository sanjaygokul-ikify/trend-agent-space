import time

class Metric:
    def __init__(self, name: str):
        self.name = name
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            print(f"{self.name}: {elapsed_time} seconds")