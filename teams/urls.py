from django.conf.urls import url, include
from django.contrib import admin
from .views import TeamsList, PlayerList, Teams, Players, search, TeamJSONList, PlayerJSONList, PlayerDetJSONList,\
    TeamDetJSONList, TeamCreate, TeamDelete, TeamUpdate, PlayersCreate, PlayersUpdate, PlayersDelete, GameList, GameRound,\
    Welcome
from .feeds import TeamListFeed, PlayerListFeed
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_swagger_view(title='Pastebin API')

app_name = 'teams'

urlpatterns = [
    url(r'^$', Welcome.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^team/$', TeamsList.as_view(), name='teams-list'),
    url(r'^team/[+]add/$', TeamCreate.as_view(), name='teams-add'), #add teams
<<<<<<< HEAD
    url(r'^json/team/(?P<slug>[\w-]+)$', TeamDetJSONList.as_view(), name='JSONteam'),
    url(r'^json/team/$', TeamJSONList.as_view()),
    url(r'^team/(?P<slug>[\w-]+)/edit/$', TeamUpdate.as_view(), name='teams-update'),
    url(r'^json/player/$', PlayerJSONList.as_view()),
    url(r'^team/(?P<slug>[\w-]+)/$', Teams.as_view(), name='team'),
=======
    url(r'^team/json/$', TeamJSONList.as_view()),
    url(r'^team/json/(?P<slug>[\w-]+)$', TeamDetJSONList.as_view(), name='TeamJSON'),
    url(r'^team/(?P<slug>[\w-]+)/edit/$', TeamUpdate.as_view(), name='teams-update'),
    url(r'^player/json/$', PlayerJSONList.as_view()),
    url(r'^team/(?P<slug>[\w-]+)/$', Teams.as_view(), name='team-detail'),
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09
    url(r'^team/(?P<slug>[\w-]+)/delete/$', TeamDelete.as_view(), name='teams-delete'),
    url(r'^player/$', PlayerList.as_view(), name='players-list'),
    url(r'^player/(?P<slug>[\w-]+)$', Players.as_view(), name='player'),
    url(r'^player/(?P<slug>[\w-]+)/edit/$', PlayersUpdate.as_view(), name='player-update'),
    url(r'^player/(?P<slug>[\w-]+)/delete/$', PlayersDelete.as_view(), name='player-delete'),
    url(r'^player/[+]add/$', PlayersCreate.as_view(), name='player-add'),
    url(r'^search/$', search),
    url(r'^team/feed/$', TeamListFeed()),
    url(r'^player/feed/$', PlayerListFeed()),
<<<<<<< HEAD
    url(r'^json/player/(?P<slug>[\w-]+)$', PlayerDetJSONList.as_view()),
=======
    url(r'^player/json/(?P<slug>[\w-]+)$', PlayerDetJSONList.as_view()),
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09
    url(r'^games/$', GameList.as_view(), name='game-list'),
    url(r'^games/(?P<slug>[0-9]+)/$', GameRound.as_view(), name='game-round'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<<<<<<< HEAD
urlpatterns = format_suffix_patterns(urlpatterns)
=======
urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09
