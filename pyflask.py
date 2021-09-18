from flask import Flask,render_template,redirect,url_for  
app = Flask(__name__)  

days=["day 1 , day 2"]
  
@app.route("/", methods=["Post","Get"])  
def message():  
      if request.method == "POST":
        user = request.form["nm"]
        password = request.form["password"]
        return redirect(url_for("user", usr=user , pwd =password))
      else:
        return render_template("log.html")  

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':  
   app.run(debug=True)  