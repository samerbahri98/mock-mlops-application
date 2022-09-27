from flask import Flask, json
from cron import job
from api import api
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", seconds=20)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())



app.register_blueprint(api)

if __name__ == '__main__':
    app.run()
