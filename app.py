from flask import Flask, render_template, request
import sqlite3

def db():
    conn=sqlite3.connect("C:\\sqlite\\AprData")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Apr (Passengers INTEGER, Range INTEGER)")
    conn.commit()
    conn.close()

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/B747.html")
def B747():
    return render_template("B747.html")

@app.route("/new.html")
def new():
    return render_template("new.html")

@app.route("/B737.html")
def B737():
    conn=sqlite3.connect("C:\\sqlite\\AprData")
    conn.row_factory=sqlite3.Row

    cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS Apr (Passengers INTEGER, Range INTEGER)")
    cur.execute("SELECT * FROM Apr")

    rows=cur.fetchall()
    return render_template("B737.html", rows=rows)

@app.route("/new_info", methods=['POST', 'GET'])
def new_info():    
    if request.method=='POST':
        try:
            Type = request.form["type"]
            Passengers = request.form["passengers"]
            Range = request.form["Range"]
            Weight = request.form["Weight"]
            MPG = request.form["MPG"]

            con = sqlite3.connect("C:\\sqlite\\AprData") 
            cur=con.cursor()
            #cur.execute("CREATE TABLE IF NOT EXISTS Apr (Passengers TEXT, Range TEXT)")
            cur.execute("INSERT INTO Apr VALUES (?,?,?,?,?)",(Type, Passengers, Range, Weight, MPG))
            con.commit()
            #con.close()               
            #msg="Success"
        except:
            con.rollback()
            #msg="error while inserting values"
        finally:
            return render_template("success.html")
            con.close()

@app.route("/update.html")
def up():
    return render_template("update.html")

@app.route("/update", methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        Type = request.form["type"]
        Passengers = request.form["passengers"]
        Range = request.form["Range"]
        Weight = request.form["Weight"]
        MPG = request.form["MPG"]

        conn = sqlite3.connect("C:\\sqlite\\AprData")
        cur=conn.cursor()
        cur.execute("UPDATE Apr SET mpg=?, Passengers=?, Range=?, Weight=? WHERE Type=?",(MPG, Passengers, Range, Weight, Type))
        conn.commit()
        conn.close()

        return render_template("success.html")

if __name__ == "__main__":
    app.debug=True
    app.run()
