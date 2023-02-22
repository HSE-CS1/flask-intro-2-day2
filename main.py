from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)

TODOS = ["Homework", "Take out the trash", "Workout", "Wash the dishes"]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/roll")
def roll():
  dice_roll = [] # the list of dice we will roll
  n = request.args.get("n", 2) # 2 would be the default value if there isn't an n
  n = int(n) # turn the n parameter int an integer
  for x in range(n): # loop n times
    die = randint(9856, 9861) # random number between for emoji codes
    dice_roll.append(chr(die)) # add the random number to the dice_roll
  return render_template("roll.html", number=n, dice_roll=dice_roll)

@app.route("/todo")
def todo():
  return render_template("todo.html", todos=TODOS)

@app.route("/add")
def add():
  return render_template("add.html")

if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)