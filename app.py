from flask import Flask, render_template, request, flash, redirect, url_for
from forms import myForm

app = Flask(__name__)

app.secret_key = "Super_sensitive"

@app.route("/", methods = ["POST", "GET"])
def form():
    form = myForm()
    if form.validate_on_submit():
        name = form.name.data
        flash(f"Hello { name }, your registered successfully.")
        return redirect(url_for("welcome"))
    
    return render_template("form.html", form=form)
    
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


if __name__ == "__main__":
    app.run(debug=True)