#####################################################
# Kaffa - Pre-qualification Test
# 7) Rest Server - World Clock
# Name: Pedro Rodrigo Ramos Morelli
# E-mail: pedromorelli96@gmail.com
#####################################################

# flask necessary to put up mock server
from flask import Flask, json

# datetime used to get current time
import datetime

# instanciation of the Flask class
# using __name__ because this works as a single module
api = Flask(__name__)

# route tells Flask what URL should trigger the
# get_current_time function
@api.route('/')
def get_current_time():

    # datetime.now gets current computer time
    tm = datetime.datetime.now()
    # we then convert it to adequate format
    format_tm = tm.strftime("%Y-%m-%dT%H:%MZ")

    # this is a simple dict that will be converted into json
    current_time = {
        "currentDateTime":format_tm
    }
    # returns the json version of the dict which contains current time
    return json.dumps(current_time)

api.run()