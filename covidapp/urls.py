from covidapp import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage),
]
