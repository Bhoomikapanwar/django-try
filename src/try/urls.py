from django.urls import path,include
from . import views

urlpatterns= [
        path('home/',views.home,name='home'),
        path('',views.home,name='home'),
        path('contact/',views.contact,name='contact'),
        path('about/',views.about,name='about'),
]
