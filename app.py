from flask import Flask, render_template, url_for, session, redirect
from flask_session import Session
from tempfile import mkdtemp
app = Flask(__name__)

#The following applications store and use cookies.
app.secret_key = "iorhqoiwrh1ior2r1rni1rno1inr"
app.config["SESSION_FILE_DIR"] =mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

#the following function contains all the possible winning combinations.
def is_winner(board):
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return "O"
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return "O"
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return "O"
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return "O"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return "X"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return "X"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return "X"
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "X"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "X"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "X"
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X"
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"
    elif board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2]:
        return "Tie"
    else:
        return None # no alert is displayed if there is no winner or tie


@app.route("/")
def index():
    if "board" not in session: # if there are no stored cookies, a default board will be made.
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "O"

    winner = is_winner(session["board"])


    return render_template("index.html", game=session["board"], turn=session["turn"], winner=winner)



@app.route("/play/<int:row>/<int:col>")
def play(row, col): # changes user input from X to O and vise versa after each turn.

    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"] = "X"

    return redirect(url_for("index", row=row, col=col))

@app.route("/reset")
def reset(): # resets game back to default board
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    return redirect(url_for("index"))

@app.route("/about_us")
def about_us():# the following code is for the About Us page
    return render_template("about_us.html")

if __name__ == '__main__':

    app.run(debug=True)
