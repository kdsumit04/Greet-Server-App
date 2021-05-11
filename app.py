from flask import Flask
import logging

app = Flask(__name__)

#below 3 lines are used to remove a unwanted info which
#was also getting printed
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
@app.route("/greeting/<name>")
def greeting(name):
    logging.info("Greet-Server is Started")
    return "Hello " + name 

if __name__ == "__main__":
    app.run(host ='0.0.0.0',port='80')





