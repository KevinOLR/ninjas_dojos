from flask import Flask, render_template, session, request, redirect
from newdojo import Dojo
from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def users():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("users.html", dojos=dojos)


@app.route('/ninjas')
def new():
    return render_template("new_user.html")

@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/create_ninja',methods=['POST'])
def create_ninja():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("users.html", dojos=dojos)   

if __name__=="__main__":
    app.run(debug=True)