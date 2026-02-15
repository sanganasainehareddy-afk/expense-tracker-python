from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

# Load expenses from file
def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount, category = line.strip().split(",")
                expenses.append((name, float(amount), category))
    except FileNotFoundError:
        pass

# Save all expenses to file
def save_all():
    with open("expenses.txt", "w") as file:
        for e in expenses:
            file.write(f"{e[0]},{e[1]},{e[2]}\n")

@app.route("/")
def index():
    total = sum([e[1] for e in expenses])
    return render_template("index.html", expenses=expenses, total=total)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    amount = float(request.form["amount"])
    category = request.form["category"]

    expenses.append((name, amount, category))
    save_all()

    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    try:
        expenses.pop(index)
        save_all()
    except:
        pass
    return redirect("/")

load_expenses()

if __name__ == "__main__":
    app.run(debug=True)