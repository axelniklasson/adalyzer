from flask import Flask
from runner import Connection

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


if __name__ == '__main__':
	c = Connection()
	c.start()
	app.run()
