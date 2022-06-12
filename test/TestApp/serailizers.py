

from rest_framework import serializers
from .models import Event, Ticket

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'



class TicketSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(many = False, view_name = 'event-show')

    class Meta:
        model = Ticket
        fields = '__all__'