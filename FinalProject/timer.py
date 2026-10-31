import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        self.end_time = time.time()

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def format(self):
        mins, secs = divmod(int(self.end_time - self.start_time), 60)
        return f"{mins}m {secs}s"