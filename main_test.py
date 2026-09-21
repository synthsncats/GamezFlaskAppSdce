from flask import Flask, render_template, request
import sqlite3 as sql
import dbcalls as mydb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view():

    # TODO create sql function to view data

    rows = [('testname', 'testaddr', 'testcity', 'testid')]
    print(rows)
    return render_template("view.html", rows=rows)

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/updaterec', methods=['POST', 'GET'])
def updaterec():
    if request.method == 'POST':
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            id = request.form['id']

            # TODO create search function and print rows

            msg = "Record with test1, test, test, test successfully added"
            return render_template("updateresult.html", message=msg)

@app.route('/seachrec', methods=['POST', 'GET'])
def searchrec():
    if request.method == 'POST':
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']

        # TODO create search function and print rows

        rows = [('testname', 'testaddr', 'testcity', 'testid')]
        print ("search", rows)
        return render_template("searchresult.html", rows=rows)

@app.route('/deleterec', methods=['POST', 'GET'])
def deleterec():
    if request.method == 'POST':
        nm = request.form['nm']

        #TODO create delete function and print msg to delete

        msg= [('testname', 'testaddr', 'testcity', 'testid')]
        print(msg)
        return render_template("deleteresult.html", message = msg)

if __name__ == '__main__':
    app.run(debug=True)