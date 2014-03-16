"""The API for crosswords."""
import json
from django.contrib.auth.decorators import login_required
from lib.response import response, error_response
from base.board import create_board, BadBoard


@login_required
def board(request):
    """
    The /api/board endpoint. Users can set up a new board here.

    """
    try:
        req_body = json.loads(request.body)
    except (ValueError, TypeError):
        return error_response('JSON parse error.')
    if request.method == 'POST':
        # Create a board.
        try:
            create_board(request.user, req_body)
        except BadBoard as exc:
            return error_response(str(exc))
        return response('OK')


def history(request):
    """
    The /api/history endpoint.
    """
    pass


def board_obj(board):
    """
    A Python obj representation of a board.
    """
    return {'tiles': json.loads(board.tiles_repr),
            'board': json.loads(board.board_repr),
            'hash': board.hash}
