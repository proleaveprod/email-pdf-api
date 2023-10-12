# import main Flask class and request object
from flask import Flask, request

GLOBAL_URL = "cantest.starline.ru"
LOCAL_URL  = "frm01-prod-can.rd.netlo"

GLOBAL_IP  = "10.100.9.12"
LOCAL_IP   = "10.50.28.238"

host_addr = LOCAL_IP
host_port = 5252

# create the Flask app
app = Flask(__name__)

@app.route('/yandex_request', methods=['POST'])
def query_example():
    return 'Hello world from cantest!!!'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host=host_addr, port=host_port, debug=True)