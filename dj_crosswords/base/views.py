# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import UserBoardThrough
from base.api import board_obj
import json


@login_required
def home(request):
    # Load any user boards.
    objs = UserBoardThrough.objects.filter(user=request.user)
    boards = [board_obj(obj.board) for obj in objs]
    return render(request, 'index.html', {
                  'boards': json.dumps(boards)
                  })
