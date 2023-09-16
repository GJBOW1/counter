from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'Almost dead yesterday, maybe dead tomorrow, but alive, gloriously alive, today.'

@app.route('/', methods=['GET', 'POST'])
def home():
    if session['count'] == 0:
        session['count'] += 1
    else: 
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session', methods=['GET', 'POST'])
def wipe():
    session.clear()
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, port=5001)
