from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create', views.create, name = 'create'),
    path('display', views.display, name = 'display'),
    path('update/<int:uid>', views.update, name = 'update'),
    path('delete/<int:uid>', views.delete, name = 'delete'),
    path('help', views.help, name = 'help'),
    path('about', views.about, name = 'about')
]