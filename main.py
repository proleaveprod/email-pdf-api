# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/yandex_request', methods=['POST'])
def query_example():
    return 'Hello world from cantest!!!'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)