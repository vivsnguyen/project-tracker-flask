"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

import hackbright

app = Flask(__name__)
app.secret_key = "something-random-here"

@app.route("/")
def index():

    return render_template("welcome.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    
    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                               first=first,
                               last=last,
                               github=github)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['GET'])
def get_student_add_form():
    """Show form for searching for a student."""

    return render_template("new_student_form.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Show form for searching for a student."""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)
    flash('New student added.')

    return render_template("confirmation-added.html", github = github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
    DebugToolbarExtension(app)
    # app.debug = True
