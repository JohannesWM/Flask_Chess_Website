from base_piece import ChessPiece
import chess
# board = chess.Board()
# board.push_san("c3")
# print(board)
#
#
# basicPiece = ChessPiece([2, 1], "black")
# basicPiece.move_position([1, 2])
# print(basicPiece.position)
move = chess.Move.from_uci("g1f3")

board = chess.Board()  # importing the python chess libarry
board.legal_moves  # create a new chess board instance
board.legal_moves.count()  # returns a dynamic list of legal moves
board.push(move)  # play a move (transforms the state of the baord)
# board.pop()  # removes the last move played
# board.piece_type_at(square)  # returns the suqr's corresponding chess piece
print(board.turn)  # returns a chess color object

board
print(board)
