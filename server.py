#import psycopg2
#import psycopg2.extras

from flask import Flask, render_template, request
app = Flask(__name__)


def connectToDB():
  connectionString = 'dbname=music user=postgres password=kirbyk9 host=localhost'
  try:
    return psycopg2.connect(connectionString)
  except:
    print("Can't connect to database")

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

@app.route('/music')
def showChart():
  """rows returned from postgres are just an ordered list"""
  
  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select artist, name from albums")
  except:
    print("Error executing select")
  results = cur.fetchall()
  return render_template('music.html', albums=results)



@app.route('/music2')
def showChartUsingPythonDictionary():
  """rows returned from postgres are a python dictionary (can
  also be treated as an ordered list)"""
  conn = connectToDB()
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  try:
    cur.execute("select artist, name from albums")
  except:
    print("Error executing select")
  results = cur.fetchall()
  print results
  return render_template('music2.html', albums=results)


@app.route('/music3', methods=['GET', 'POST'])
def showChartForms():
  """rows returned from postgres are a python dictionary (can
  also be treated as an ordered list)"""
  conn = connectToDB()
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  if request.method == 'POST':
    # add new entry into database
    try:
      cur.execute("""INSERT INTO albums (artist, name, rank) 
       VALUES (%s, %s, %s);""",
       (request.form['artist'], request.form['album'], request.form['rank']) )
    except:
      print("ERROR inserting into albums")

  try:
    cur.execute("select artist, name from albums")
  except:
    print("Error executing select")
  results = cur.fetchall()
  for r in results:
    print r['artist']
  return render_template('music3.html', albums=results)



if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
