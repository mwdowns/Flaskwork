from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname="phonebook_db")
app = Flask("PhonebookApp")

@app.route("/")
def landing():
    return render_template(
    "index.html",
    title="Welcome to the Phonebook",
    )

@app.route("/phonebook")
def phonebook():
    query = db.query("select * from phonebook")

    return render_template(
    "phonebook.html",
    title="Phonebook entries",
    entries_list=query.namedresult()
    )

@app.route("/new_entry")
def entry():
    return render_template(
    "entry.html",
    title="New Entry"
    )

@app.route("/new_entry", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    phone_number = request.form.get("phone_number")
    email = request.form.get("email")
    db.insert(
        "phonebook",
        name=name,
        phone_number=phone_number,
        email=email
    )
    return redirect("/")

@app.route("/update")
def update():
    query = request.args.get("query")
    if query:
        entry = db.query("select * from phonebook where name ilike '%s'" % query)
        return render_template(
        "update.html",
        title="Update Entry",
        to_be_updated=entry.namedresult()
        )
    else:
        return render_template(
        "update.html",
        title="Update Entry"
    )

# @app.route("/update", methods=["POST"])
# def submit_form():
#     name = request.form.get("name")
#     phone_number = request.form.get("phone_number")
#     email = request.form.get("email")
#     db.update(
#         "phonebook",
#
#     )


if __name__ == "__main__":
    app.run(debug=True)
