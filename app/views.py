from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO = TopicForm()
    d = {'ETFO':ETFO}
    if request.method=='POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['topic_name']
            TO = Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse("Topic inserted successfully")
        else:
            return HttpResponse("Invalid Data")
        
    return render(request,'insert_topic.html',d)    


def insert_webpage(request):
    EWFO = WebpageForm()
    d = {'EWFO': EWFO}
    if request.method=='POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            tn = WFDO.cleaned_data['topic_name']
            TO = Topic.objects.get(topic_name = tn)
            name = WFDO.cleaned_data['name']
            url = WFDO.cleaned_data['url']
            email = WFDO.cleaned_data['email']
            
            WO = Webpage.objects.get_or_create(topic_name = TO,name=name,url = url,email=email)[0]
            WO.save()
            return HttpResponse("Webpage inserted successfully")
        else:
            return HttpResponse('Invalid Data')
        
    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    EAFO = AccessrecordForm()
    d = {'EAFO':EAFO}
    if request.method=='POST':
        AFDO = AccessrecordForm(request.POST)
        if AFDO.is_valid():
            name = AFDO.cleaned_data['name']
            WO = Webpage.objects.get(pk=name)
            date = AFDO.cleaned_data['date']
            author = AFDO.cleaned_data['author']
            AO = Accessrecord.objects.get_or_create(name=WO,date=date,author=author)[0]
            AO.save()
            return HttpResponse("Accessrecord Inserted successfully")
        else:
            return HttpResponse("Invalid Data")
    return render(request,'insert_accessrecord.html',d)