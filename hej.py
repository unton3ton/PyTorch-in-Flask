from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return "Hoi" # http://192.168.100.90:5000/hello

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)

'''
$ python hej.py 
 * Serving Flask app 'hej'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.100.90:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-788-518

192.168.1.121 - - [30/Jan/2025 12:26:18] "GET / HTTP/1.1" 200 -
'''