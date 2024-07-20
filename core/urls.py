from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_tour, name='home'),
    path('/tours', views.show_tours, name='show_tours')
    ]
