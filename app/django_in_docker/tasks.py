import time

from .celery import app

@app.task
def test_task():
    for i in range(100):
        print(f'=========== {i}')
        time.sleep(2)
