from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.AddPost.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostRead.as_view(), name='post_detail'),
    path('<slug:slug>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
]

handler404 = 'board_ohm.views.handler404'
handler500 = 'board_ohm.views.handler500'