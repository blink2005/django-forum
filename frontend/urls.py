from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('registration/', views.registration),
    path('logout/', views.logout),
    path('user/<int:id>/', views.user),
    path('changephoto/', views.change_photo),
    path('createpost/', views.create_post),
    path('thread/<int:id>/', views.thread)
]
