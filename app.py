from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    logging.info("We are checking logging files")
    return "CI CD Pipeline has been established successfully"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


