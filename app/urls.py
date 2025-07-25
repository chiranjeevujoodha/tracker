from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_home' ),
    path('save-session/', views.save_session_ajax, name='save-session'),
    path('api/sessions/', views.sessions_list, name='sessions-list'),
]
