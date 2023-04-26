import os
from datetime import datetime


class Logger():

    log_file = None

    def __init__(self):
        time_now = round((datetime.now() - datetime(1970, 1, 1)).total_seconds())
        print(time_now)
        try:
            os.mkdir("./logs")
        except FileExistsError:
            pass
        self.log_file = open(f"./logs/log_{time_now}.log", 'x')

    def log(self, log_message: str):
        time_now = datetime.now()
        self.log_file.write(f"In time {time_now} print this message => {log_message}\n\n")
        self.log_file.flush()
        #os.fsync(self.log_file.fileno())

    def __del__(self):
        if self.log_file is not None:
            self.log_file.close()
        print("I'm being automatically destroyed. Goodbye!")
