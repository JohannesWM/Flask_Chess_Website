from flask import render_template, request
from app import app
from chess_pieces import base_piece as bp

piece1 = bp.ChessPiece([0, 0], "white")


@app.route('/')
@app.route('/index')
def index():
    return render_template('chess.html', position=piece1.position)


@app.route("/update_center_text", methods=["POST"])
def update_center_text():
    new_text = request.form.get("text")
    # print(new_text)
    # perform some operation to update the center text object

    return new_text

@app.route("/update_board", methods=["POST"])
def update_board():
    new_text = request.form.get("text")
    print(new_text)
    return new_text

