from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

tasks = []  # Хранение задач в памяти


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("task")
    if text:
        tasks.append({
            "text": text,
            "done": False,
            "created_at": datetime.now().strftime("%d.%m.%Y %H:%M")
        })
    return redirect("/")


@app.route("/toggle/<int:index>")
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
    return redirect("/")


@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")


@app.route("/clear_done", methods=["POST"])
def clear_done():
    global tasks
    tasks = [task for task in tasks if not task["done"]]
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
