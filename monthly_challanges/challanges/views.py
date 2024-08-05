from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challanges = {
    'january': 'Eat No Meat for the entire month!',
    'february': 'Walk for at least 20 min every day!',
    'march': 'Learn Django for at least 20 min every day!',
    'april': 'april challange',
    'may': 'may challange',
    'june': 'june challange',
    'july': 'july challange',
    'august': 'august challange',
    'september': 'september challange',
    'octomber': 'octomber challange',
    'november': 'november challange',
    'december': 'december challange',
}

# Create your views here.
def monthly_challange_by_number(request, month):
    return HttpResponse(month)

def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
    except:
        return HttpResponseNotFound('Month isnt Supported!')
    
    return HttpResponse(challange_text)