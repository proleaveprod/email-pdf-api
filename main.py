# import main Flask class and request object
from flask import Flask, request, render_template

GLOBAL_URL = "cantest.starline.ru"
LOCAL_URL  = "frm01-prod-can.rd.netlo"

LOCALHOST  = "0.0.0.0"
GLOBAL_IP  = "10.100.9.12"
LOCAL_IP   = "10.50.28.238"

host_addr = LOCALHOST
host_port = 80

# create the Flask app
app = Flask(__name__)

@app.route('/yandex_request', methods=['POST'])
def query_example():
    return 'Hello world from cantest!!!'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html'), 200



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host=host_addr, port=host_port, debug=True)