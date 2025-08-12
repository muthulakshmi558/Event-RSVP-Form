from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# RSVP Form Class
class RSVPForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    will_attend = BooleanField("I will attend")
    submit = SubmitField("Submit RSVP")

@app.route("/", methods=["GET", "POST"])
@app.route("/rsvp", methods=["GET", "POST"])
def rsvp():
    form = RSVPForm()
    if form.validate_on_submit():
        if form.will_attend.data:
            flash("Great! We’re excited to see you at the event.", "success")
        else:
            flash("Sorry to miss you! Maybe next time.", "error")
        return redirect(url_for("rsvp"))
    return render_template("rsvp.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
