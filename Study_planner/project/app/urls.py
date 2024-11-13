from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('timetable/', views.timetable, name='timetable'),  # Timetable view
    path('analytics/', views.analytics, name='analytics'),  # Analytics view
]
