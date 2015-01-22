from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def mainIndex():
    return render_template('index.html', selectedMenu='Home')

@app.route('/report')
def report():
  return render_template('report.html', selectedMenu='Report')

@app.route('/report2', methods=['POST'])
def report2():
  abduction = {'firstname': request.form['firstname'],
               'lastname': request.form['lastname']}
  return render_template('report2.html', abduction = abduction)

@app.route('/simple')
def simple():
  return render_template('simple.html')

@app.route('/simple2', methods=['POST'])
def simple2():
  return render_template('simple2.html')


@app.route('/simple3')
def simple3():
  return render_template('simple3.html')

@app.route('/simple4', methods=['POST'])
def simple4():
  return render_template('simple4.html', name=request.form['name'])



if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
