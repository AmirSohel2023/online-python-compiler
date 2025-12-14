from flask import Flask, render_template, request
import io
import contextlib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    code = ""
    output = ""

    if request.method == "POST":
        code = request.form.get("code")

        try:
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                exec(code, {})   # executes Python code
            output = buffer.getvalue()

        except Exception as e:
            output = str(e)

    return render_template("index.html", code=code, output=output)


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
