from django.http import JsonResponse
from django.shortcuts import render
from .models import Event
from .serailizers import EventSerializer

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer)