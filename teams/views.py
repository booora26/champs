from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Team, Player, Game
from django.template import Context, Template
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeamSerializer, PlayerSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core.urlresolvers import reverse_lazy
<<<<<<< HEAD
from rest_framework.renderers import JSONRenderer
=======
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09



# Create your views here.

class Welcome(TemplateView):
    template_name = 'teams/index.html'


class TeamsList(ListView):

    model = Team
    template_name = 'teams/team_list.html'
    context_object_name = 'team_list'
    queryset = Team.objects.order_by('name')


class TeamJSONList(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'country', 'arena']


class PlayerList(ListView):
    model = Player
    template_name = 'teams/player_list.html'
    context_object_name = 'player_list'
    paginate_by = 20
    queryset = Player.objects.order_by('first_name')

# class PlayerJSONList(APIView):
#
#     def get(self, request):
#         players = Player.objects.all()
#         serializer = PlayerSerializer(players, many=True)
#         return Response(serializer.data)


class PlayerJSONList(ListAPIView):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['born','first_name', 'height', 'last_name', 'nationality', 'number', 'position', 'club__name']
    #permission_classes = [IsAuthenticated, IsAdminUser]


class Teams(DetailView):
    model = Team
    query_pk_and_slug = Team.slug
    template_name = 'teams/team.html'
    context_object_name = 'team'
    queryset = Team.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Teams, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['player_list'] = Player.objects.all().filter(club__slug = self.kwargs['slug'])
        context['game_list'] = Game.objects.filter(Q(home_team__slug = self.kwargs['slug']) | Q(away_team__slug = self.kwargs['slug']))
        #context['game_list'] = Game.objects.all().filter(away_team__slug = self.kwargs['slug'])
        return context


class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'country', 'arena', 'website', 'logo']


class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'country', 'arena', 'website', 'logo', 'flag']


class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('teams:teams-list')


class TeamDetJSONList(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'slug'
<<<<<<< HEAD
    renderer_classes = (JSONRenderer,)
=======
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09


class Players(DetailView):
    model = Player
    query_pk_and_slug = Player.slug
    template_name = 'teams/player.html'
    context_object_name = 'player'
    queryset = Player.objects.all()


class PlayersCreate(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'position', 'number', 'height', 'born', 'nationality', 'pic', 'club']


class PlayersUpdate(UpdateView):
    model = Player
    fields = ['first_name', 'last_name', 'position', 'number', 'height', 'born', 'nationality', 'pic', 'club']


class PlayersDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('teams:players-list')

class PlayerDetJSONList(RetrieveAPIView):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'slug'


class GameList(ListView):
    model = Game
    # context_object_name = 'game_list'
    template_name = 'teams/game_list.html'
    # queryset = Game.objects.order_by('-round')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GameList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['game_list'] = Game.objects.order_by('-round')
        context['game_round'] = Game.objects.values_list('round').distinct()
        return context



class GameRound(ListView):
    model = Game
    template_name = 'teams/game_small.html'
    slug_field = 'round'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GameRound, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['game_list'] = Game.objects.filter(round = self.kwargs['slug'])
<<<<<<< HEAD
        context['game_round'] = Game.objects.values_list('round').distinct()
=======
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09
        return context



def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            player= Player.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) )
            team= Team.objects.filter(name__icontains=q)
            return render_to_response('teams/search_results.html',
                                      {'players': player, 'teams': team, 'query': q})
    return render_to_response('teams/search_form.html',
                              {'errors': errors})

