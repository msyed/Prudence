#web application framework written in python
from flask import Flask, abort, session, request, url_for, make_response, redirect, render_template

#create a flask instance 
app = Flask(__name__)

# secret keyq
app.secret_key = '\xd3\xbdMBJ\xbb\xfe\x8d\xe4\xe9\xb8\x15\xde]\xd9ei\xfb\x8f1\xb2=O\x16'

#render homepage
@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
	return render_template('question.html')



#run app and use debugger to check Flask errors  
if __name__ == '__main__':
	app.run(debug = True)

