from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import Event, Ticket
from .serailizers import EventSerializer, TicketSerializer, UserSerializer
from django.contrib.auth.models import User
from abc import ABC
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventList(generics.ListCreateAPIView):
    """
    To be used when displaying a series of events when a user searches for them, in accordance with a series of search parameters.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self,request):
        EventList.serializer.save(organiser = self.request.user)

class EventCreate(generics.CreateAPIView):
    """
    To be used by an organiser to create an event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    To be used 
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TicketList(generics.ListCreateAPIView):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketEventView(generics.GenericAPIView):
    queryset = Ticket.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self,request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        ticket = self.get_object()
        ticket = TicketSerializer(ticket,context = serializer_context)
        return Response(ticket.event)

    

def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe = False)

def event_create(request):
    data = JSONParser().parse(request)
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.errors, status = 400)

def event_show(request,event_id):
    event = Event.objects.get(id=event_id)
    serializer = EventSerializer(event,many = False)
    return JsonResponse(serializer.data, safe = False)



def ticket_list(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return JsonResponse(serializer.data, safe = False)

def ticket_create(request):
    data = JSONParser().parse(request)
    print(data)
    serializer = TicketSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        print("here")
        serializer.save()
        return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.errors, status = 400)

def ticket_show(request,ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    serializer = TicketSerializer(ticket,many = False)
    return JsonResponse(serializer.data, safe = False)



