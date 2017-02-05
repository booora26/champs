<<<<<<< HEAD
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09
=======
>>>>>>> c6062dea30b9485e36418238648b0b342809b43c
from .models import Team, Game


def teams(context):
    return {'teams': Team.objects.all()}


def games(context):
    return {'games': Game.objects.all()}