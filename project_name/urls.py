from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/',views.event_list)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        
    ] + urlpatterns
