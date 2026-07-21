from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Simple Bank</title>
<h2>Simple Bank Web App</h2>
<form method="post">
  Full Name: <input name="name"><br><br>
  Amount(Deposit): <input name="amount" type="number"><br><br>

 
  <button type="submit">Deposit</button>
</form>
{% if message %}
<p><b>{{ message }}</b></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        amount = request.form.get("amount")
        if name and amount:
            message = f"₹{amount} deposited successfully for {name}"
        else:
            message = "Please enter name and amount"
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run()
