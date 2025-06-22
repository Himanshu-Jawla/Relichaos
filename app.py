from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/preorder", methods=["GET", "POST"])
def preorder():
    if request.method == "POST":
        
        return redirect("/success")
    return render_template("preorder.html")

@app.route("/success")
def success():
    return render_template("success.html")
    
if __name__ == "__main__":
    app.run(debug=True)
