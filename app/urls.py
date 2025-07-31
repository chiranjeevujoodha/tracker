from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_home' ),
    path('create-session/', views.create_session, name='create_session'),
    
]
