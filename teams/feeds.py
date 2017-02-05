from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Team, Player


class TeamListFeed(Feed):
    title = "Teams feed"
    link = "/teams/"
    description = "All teams compiting in Euroleague."

    def items(self, obj):
        return Team.objects.order_by('name')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.country

    def item_link(self, item):
        return item.get_absolute_url()


class PlayerListFeed(Feed):
    title = "Players feed"
    link = "/player/"
    description = "All players competing in Euroleague."

    def items(self, obj):
        return Player.objects.filter(nationality = 'Serbia')

    def item_title(self, item):
        return '{} {}'.format(item.first_name, item.last_name)

    def item_description(self, item):
        return item.club

    def item_link(self, item):
        return item.get_absolute_url()
