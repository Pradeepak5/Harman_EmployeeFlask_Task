from flask import Flask, render_template

employee=Flask(__name__)

@employee.route("/")
def Employee_details():
    return render_template("empdetail.html")

@employee.route("/search")
def Search():
    return render_template("search.html")

@employee.route("/update")
def Update():
    return render_template("update.html")

@employee.route("/delete")
def Delete():
    return render_template("delete.html")

if __name__=="__main__":
    employee.run()