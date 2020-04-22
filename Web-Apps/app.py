from flask import Flask, request, render_template, Response, session, redirect, url_for, redirect
from scripts.alg import algorithm
app = Flask(__name__)

@app.route('/')
@app.route('/main', methods=['POST', 'GET'])
def main():
    answer = []
    if request.method == 'POST':
        r1 = request.form['location']
        r2 = request.form['action']
        r3 = request.form['sign']
        r4 = request.form['mood']
        r5 = request.form['age']

        result = [r1, r2, r3, r4, r5]
        answer = algorithm(result)
        print(answer)

        if len(answer) > 1:
            answer = str(answer)
        else:
            answer = answer[0]

        return render_template('resultpage.html', answer = answer)
    return render_template('index.html', answer = answer)

@app.route('/results')
def results():
    return render_template('resultpage.html')



if __name__ == "__main__":
    app.run(debug=True)
