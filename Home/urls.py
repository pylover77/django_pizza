from Home import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/',views.menu, name="menu"),
    path('signup/',views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('orders/', views.orders, name="orders"),
    path('increament/', views.increament, name="increament"),
    path('decreament/', views.decreament, name="decreament")
]
