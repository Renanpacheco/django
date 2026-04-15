from django.urls import path

from . import views
from .views import index

urlpatterns = [
    #path("", views.index, name="index"),
    #path("", index),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
]