"""
The board, etc models needed for the game.
"""
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    """
    A board is actually a game board and a set of tiles.
    """
    board_repr = models.TextField()
    tiles_repr = models.TextField()
    # A user can have many boards and a board can be used by multiple
    # users.
    users = models.ManyToManyField(User, through='UserBoardThrough')
    # The SHA-1 hash of the board and tile representation. SHA-1 may be
    # "weak" but if it's good enough for Git it's good enough for me.
    hash = models.CharField(max_length=40, db_index=True)


class UserBoardThrough(models.Model):
    user = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    # What nickname does this user call the board?
    nickname = models.CharField(max_length=5)


class SavedGame(models.Model):
    players = models.ManyToManyField(User)
    date_played = models.DateTimeField()
    # The gcg should have a representation of the board as well.
    gcg = models.TextField()
    description = models.CharField(max_length=256)
    rated = models.BooleanField(default=False)
