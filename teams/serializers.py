from rest_framework import serializers
from .models import Team, Player



class TeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='teams:TeamJSON', lookup_field='slug')

    class Meta:
        model = Team
        fields = ('name', 'country', 'arena', 'players', 'url','slug')


class PlayerSerializer(serializers.ModelSerializer):
    club = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'

    def get_club(self, obj):
        return str(obj.club.name)


