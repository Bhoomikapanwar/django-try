from django.urls import path,include
from .views import home, contact, about, ContactView,AboutTemplateView,HomeTemplateView
from django.views.generic import TemplateView

urlpatterns= [
        #using function based views
        #path('home/',home,name='home'),
        #path('',home,name='home'),
        #path('contact/',contact,name='contact'),
        #path('about/',about,name='about'),

        #using class based views
        path('contact/',ContactView.as_view(),name='contact'),

        #using class based template view
        path('about/',AboutTemplateView.as_view(),name='about'),
        path('home/',HomeTemplateView.as_view(),name='home1'),

        #another efficient way of using class based template view but here context is not there
        path('',TemplateView.as_view(template_name="home.html"))
]
