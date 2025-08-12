from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Length
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

class ReviewForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    rating = IntegerField("Rating (1-5)", validators=[DataRequired(), NumberRange(min=1, max=5, message="Rating must be between 1 and 5")])
    review = TextAreaField("Review Message", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Submit Review")

@app.route("/", methods=["GET", "POST"])
@app.route("/review", methods=["GET", "POST"])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        flash("Thank you for your review!", "success")
        return redirect(url_for("review"))
    return render_template("review.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
