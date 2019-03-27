from flask import Flask  
from flask import render_template
from flask import request
from logging.config import dictConfig

import logging
logging.basicConfig(filename='app.log',level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Loading the index page")
    return render_template('index.html')

@app.route("/diagostics", methods=['POST'])
def diagostics():
    # Log to HEC??

    # Log to file.
    print(request.data)
    app.logger.info(request.data)
    return "OK"


if __name__ == "__main__":  
    app.run(debug=True)