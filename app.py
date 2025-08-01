from flask import Flask, render_template, request
from scanner.scanner import run_scans

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        target_url = request.form.get("url")
        output = run_scans(target_url)
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
