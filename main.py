from flask import Flask
import time 
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    return "<p>Hello, World!</p>"
#Write a func to generate a number between 0 to 10^7 and sleep  between 0-20
@app.route("/gen_num")
def genum():
    num = random.randint(0,10**7+1)
    timesleep = random.randint(0,4)
    time.sleep(timesleep)
    return {
        "random_number" : num,
    }