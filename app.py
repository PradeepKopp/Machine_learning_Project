from flask import Flask
from housing.logger import logging
import sys
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custum exception")
    except Exception as e:
        housing =HousingException(e,sys) 
        logging.info(housing.error_message)
        logging.info("We are checking logging files")
    return "CI CD Pipeline has been established successfully"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


