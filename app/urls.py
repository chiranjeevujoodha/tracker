from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_home' ),
    path('exercises/', views.exercises, name='exercises' ),
    path('calendar/', views.calendar_view, name='calendar_view' ),
    path('create-session/', views.create_session, name='create_session'),
    
]
