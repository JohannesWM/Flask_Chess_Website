from base_piece import ChessPiece

basicPiece = ChessPiece([2, 1], "black")
basicPiece.move_position([1, 2])
print(basicPiece.position)
