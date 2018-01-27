from django.urls import path,include
from .views import home, contact, about, ContactView

urlpatterns= [
        #using function based views
        path('home/',home,name='home'),
        path('',home,name='home'),
        #path('contact/',contact,name='contact'),
        path('about/',about,name='about'),

        #using class based views
        path('contact/',ContactView.as_view(),name='contact'),
]
