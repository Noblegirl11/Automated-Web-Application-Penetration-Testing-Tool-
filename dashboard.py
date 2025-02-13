from flask import Flask, render_template, request
from web_scanner import start_scan  # Import the start_scan function from web_scanner.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target_url = request.form.get("target_url")
        if target_url:
            results = start_scan(target_url)  # Trigger the scan on the target URL
            return render_template("dashboard.html", results=results, target_url=target_url)
    return render_template("dashboard.html", results=None)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
