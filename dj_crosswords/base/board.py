"""Logic for creating, handling boards, etc."""
from base.models import Board, UserBoardThrough
import hashlib
import json


class BadBoard(Exception):

    """An exception raised if the created board has bad parameters."""

    pass


def create_board(user, body):
    if 'tiles' not in body or 'board' not in body:
        raise BadBoard('Missing "tiles" or "board".')
    board_repr = json.dumps(body['board'], sort_keys=True)
    tiles_repr = json.dumps(body['tiles'], sort_keys=True)
    # Create the hash by concatenating both these strings.
    hash = hashlib.sha1(board_repr + tiles_repr).hexdigest()
    board, created = Board.get_or_create(hash=hash,
                                         board_repr=board_repr,
                                         tiles_repr=tiles_repr)

    through = UserBoardThrough(user=user, board=board,
                               nickname=body.get('nickname', 'board'))
    through.save()
