from flask import Flask, render_template
app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template(
    "hello.html",
    title="Hello world!"
    )

if __name__ == "__main__":
    app.run(debug=True)
