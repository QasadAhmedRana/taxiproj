from django.urls import path
from . import views
from .views import ContactSuccessView, ContactView


app_name = 'homeapp'
urlpatterns = [
    #ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    path('/contact/', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('datenschutz/', views.datenschutz, name='datenschutz'),


]