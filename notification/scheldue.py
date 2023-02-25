import threading
import schedule
import time


def schedule_run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule_thread = threading.Thread(target=schedule_run_pending, daemon=True)

i = 10
def f():
    global i
    print(i)
    i = i + 10


schedule.every(10).seconds.do(f)



