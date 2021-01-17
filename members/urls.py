from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name="index"),
        path('year',views.year, name="year"),
        path('video1',views.video1, name="video1"),
        path('video2',views.video2, name="video2"),
        path('main',views.main, name="main")
]
