from django.conf import settings
from django.urls import path,include
from Forum import views

urlpatterns = [
    path('', views.Forum, name="Forum"),
    path('<int:forum_id>/', views.comments, name="comments"),

]