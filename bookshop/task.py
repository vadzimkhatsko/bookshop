from celery import Celery
import logging
logger = logging.getLogger("django") 
from time import sleep

app = Celery('myproject', broker='redis://localhost:6379/0') 
app.conf.result_backend='redis://localhost:6379/0'

@app.task
def test_fun(pause):
    sleep(pause)
    logger.error("ololo Error from celery")
    return "Done from celery"

@app.task
def test_sched():
    return 'ggfgfgfgffg'

app.conf.beat_schedule = {
        "myproject":{
            "task":"bookshop.task.test.sched",
            "schedule":30.0,
            }
        }
