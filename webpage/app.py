from flask import Flask, render_template, request
import connection.client as cl

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        if "start" in request.form:
            action = "start"
            status = 'WELCOME TO THE DARK SIDE'
        elif "stop" in request.form:
            action = "stop"
            status = 'BYE BYE'
        else:
            action = "undef"
            status = ""

        # Grab task and put in db
        userInput = request.form['email']
        passInput = request.form['password']

        cl.send(userInput, passInput, action)

        return render_template('index.html', status=status)
    else:
        # Looking at the page
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
