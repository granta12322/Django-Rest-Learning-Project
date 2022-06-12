from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import Event, Ticket
from .serailizers import EventSerializer, TicketSerializer
from abc import ABC

# Create your views here.


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

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
    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.errors, status = 400)

def ticket_show(request,ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    serializer = TicketSerializer(ticket,many = False)
    return JsonResponse(serializer.data, safe = False)



