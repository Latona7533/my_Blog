from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_view),
    path('post/<int:pk>/', views.post_view, name='post_detail')
]
