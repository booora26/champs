import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "champsleague.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from teams.models import Player, Team
from django.template.defaultfilters import slugify

# for obj in Player.objects.all():
#     obj.slug = '-'.join((slugify(obj.first_name), slugify(obj.last_name)))
#     obj.save()

# for obj in Team.objects.all():
#     obj.slug = slugify(obj.name)
#     obj.save()

for obj in Player.objects.all():
    obj.first_name = obj.first_name.capitalize()
    obj.last_name = obj.last_name.capitalize()
    obj.flag = '/media/flags/32/' + obj.nationality + '.png'
    obj.save()

for obj in Team.objects.all():
    obj.name = obj.name.replace('\r\n','')
    obj.logo = '/media/club_logos/' + obj.name + '.png'
    obj.save()

# for obj in Team.objects.all():
#     obj.logo = '/media/club_logos/' + obj.name + '.png'
#     obj.save()

# for obj in Player.objects.all():
#     obj.flag = '/media/flags/32/' + obj.nationality + '.png'
#     obj.save()
