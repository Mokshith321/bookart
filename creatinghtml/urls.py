from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/',views.booking, name ='booking'),
    path('renting/',views.renting, name ='renting'),
    path('renting/renting',views.renting, name ='renting'),
    path('about/',views.about, name ='about'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
]
