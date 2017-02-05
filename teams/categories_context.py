from .models import Team, Game


def teams(context):
    return {'teams': Team.objects.all()}


def games(context):
    return {'games': Game.objects.all()}