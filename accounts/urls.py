from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
    # path('accounts/login/',views.login,name='login'),
    
    path('booking/login',views.login,name='booking_login'),
    path('booking/register', views.register, name='booking_register'),
    path('booking/logout',views.logout,name = 'booking_logout'),
    
    path('renting/login',views.login,name='renting_login'),
    path('renting/register', views.register, name='renting_register'),
    path('renting/logout',views.logout,name = 'renting_logout'),
    
    path('about/login',views.login,name='about_login'),
    path('about/register', views.register, name='about_register'),
    path('about/logout',views.logout,name = 'about_logout'),
]
