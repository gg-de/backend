from django.urls import path

from . import views

urlpatterns = [
    path('mount_schedule/', views.ScheduleView.mount_schedule),
]