from flask import Flask

app = Flask(__name__)
from app import views
from app import solenoid
from app import ultrasonic
from app import lights