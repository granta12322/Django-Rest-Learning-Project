from rest_framework.decorators import action
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.parsers import JSONParser
from rest_framework import generics, viewsets
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


class EventViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(context = {'request': request})
        return JsonResponse(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk = pk)
        serializer = EventSerializer(event,context = {'request': request})

    def perform_create(self):
        queryset = Event.objects.all()
        serializer = EventSerializer(data = self.request.data)
        serializer.save(organiser = self.request.user)


class UserViewSet(viewsets.ModelViewSet):

    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(context = {'request': request})
        return JsonResponse(serializer.data)
    
    
    def retrieve(self, request, pk = None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = UserSerializer(user,context = {'request': request})

   


class TicketViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketSerializer(context = {'request': request})
        return JsonResponse(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, pk = pk)
        serializer = TicketSerializer(ticket,context = {'request': request})

    def perform_create(self,serializer):
        serializer.save()


        


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

    def get(self,request, *args, **kwargs):
        ticket = self.get_object()
        ticket = TicketSerializer(ticket,context = {'request': request})
        return JsonResponse(ticket.event)

    

def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True,context = {'request': request})
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
    serializer = EventSerializer(event,many = False, context = {'request': request})
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



