from flask import Flask, render_template, redirect, url_for, flash, abort, request, jsonify, send_from_directory
from flask_bootstrap import Bootstrap
import sys

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=["GET", "POST"])
def home():
    output="hellow world"
    if request.method == "POST":
        print(request.form["code"])
        try:
            codeareadata = request.form["code"]
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')  # change the standard output to the file we created
            exec(codeareadata)  # example =>   print("hello world")
            sys.stdout.close()
            sys.stdout = original_stdout  # reset the standard output to its original value
            output = open('file.txt', 'r').read()
        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e

        return render_template("index.html",output=output)
    return render_template("index.html",output=output)




if __name__ == "__main__":
    app.run(debug=True)

