from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('timetable/', views.timetable, name='timetable'),
    path('analytics/', views.analytics, name='analytics'),
]
