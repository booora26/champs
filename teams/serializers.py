from rest_framework import serializers
from .models import Team, Player


<<<<<<< HEAD
<<<<<<< HEAD
class TeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='teams:JSONteam', lookup_field='slug')
=======
=======
>>>>>>> c6062dea30b9485e36418238648b0b342809b43c

class TeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='teams:TeamJSON', lookup_field='slug')
<<<<<<< HEAD
>>>>>>> ac2249bbb4fada9f19a7fc9aed2aaea697828d09
=======
>>>>>>> c6062dea30b9485e36418238648b0b342809b43c

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


