import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#function based views
def home(request):
    num = random.randint(0,1000)
    check = True               #is used in html to conditional rendering of html tags
    myvar = "it works"
    list1= [random.randint(0,1000000),random.randint(0,100000),random.randint(0,100000)]    #will be used for iterating in html
    context = {'myvar':myvar,'num':num, 'check':check,'list1':list1}                 #context dict passed as context to render
    return render(request,"base.html",context)       #rendering htmls from template folder
    #return HttpResponse('hello welcome to home')   #simple HttpResponse
