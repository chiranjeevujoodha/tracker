from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_home' ),
    path('/exercises', views.exercises, name='exercises' ),
    path('create-session/', views.create_session, name='create_session'),
    
]
