from flask import render_template, request
from app import app
import chess
import textwrap
import html

board = chess.Board()


@app.route('/')
@app.route('/index')
def index():
    return render_template('dragChess_Feb_24.html', fen_string=board.fen())


@app.route("/update_center_text", methods=["POST"])
def update_center_text():
    new_text = request.form.get("text")
    # print(new_text)
    # perform some operation to update the center text object

    return new_text


@app.route("/update_board", methods=["POST"])
def update_board():
    chess_move_text = request.form.get("text")

    move = chess.Move.from_uci(str(chess_move_text))

    if move in board.legal_moves:
        board.push(chess.Move.from_uci(str(chess_move_text)))
    else:
        "ERROR"

    print(chess_move_text)
    print(board)

    wrapped_board = "\n".join(textwrap.wrap(str(board), width=16))

    # return html.unescape("&#9818;")
    # return wrapped_board
    return board.fen()
