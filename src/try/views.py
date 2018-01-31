import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View       #for class based view
from django.views.generic import TemplateView


#function based views
def home(request):
    num = random.randint(0,1000)
    check = True               #is used in html to conditional rendering of html tags
    myvar = "it works"
    list1= [random.randint(0,1000000),random.randint(0,100000),random.randint(0,100000)]    #will be used for iterating in html
    context = {'myvar':myvar,'num':num, 'check':check,'list1':list1}                 #context dict passed as context to render
    return render(request,"home.html",context)       #rendering htmls from template folder
    #return HttpResponse('hello welcome to home')   #simple HttpResponse

def models_list_view(request):
    l= ['logistic regression','shallow neural net','deep neural net']
    return render(request,"try/models_list.html",{'l':l})

#used to show template inheritance
def contact(request):
    context = {}
    return render(request,"contact.html",context)

def about(request):
    context = {}
    return render(request,"about.html",context)

#class based view
class ContactView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"contact.html",{})
#class based template view
class AboutTemplateView(TemplateView):
    template_name = 'about.html'

#class based template view overriding get_context_data method
class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,*args,**kwargs):
        context= super(HomeTemplateView,self).get_context_data(*args,**kwargs)
        num = random.randint(0,1000)
        check = True               #is used in html to conditional rendering of html tags
        myvar = "it works"
        list1= [random.randint(0,1000000),random.randint(0,100000),random.randint(0,100000)]    #will be used for iterating in html
        context = {'myvar':myvar,'num':num, 'check':check,'list1':list1}
        return context
