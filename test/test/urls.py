"""test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestApp import views


urlpatterns = [
    path('',views.api_root,name='root'),
    path('admin/', admin.site.urls),
    path('events/', views.event_list, name = "event-list"),
    path('event/<int:event_id>/',views.event_show, name = "event-show"),
    path('ticket/<int:ticket_id>/event',views.TicketEventView.as_view(), name = "ticket_event-show"),
    path('event_create/',views.event_create, name = "event-create"),
    path('tickets/', views.ticket_list, name = "ticket-list"),
    path('ticket/<int:ticket_id>',views.ticket_show, name = "ticket-show"),

    path('ticket_create/',views.ticket_create, name = "ticket-create"),
    path('users/', views.UserList.as_view(), name = "user-list"),
    path('user/<int:user_id>',views.UserDetail.as_view(), name = "user-show")
]
