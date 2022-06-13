

from rest_framework import serializers
from .models import Event, Ticket
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many = True, queryset = Event.objects.all())
    class Meta:
        model = User
        field = ['id','username','events']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    organiser = serializers.HyperlinkedRelatedField( view_name='user-show', read_only = True)

    class Meta:
        model = Event
        fields = '__all__'




class TicketSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(view_name='event-show', read_only = True)

    class Meta:
        model = Ticket
        fields = '__all__'