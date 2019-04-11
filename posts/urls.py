from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.list, name="list"),
    path('create/', views.create, name='create'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
]