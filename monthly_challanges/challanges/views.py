from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challange(request, month):
    if month == 'january':
        challange_text = 'january challange'
    elif month == 'february':
        challange_text = 'february challange'
    elif month == 'march':
        challange_text = 'march challange'
    else:
        return HttpResponseNotFound('Month is not supported')
    return HttpResponse(challange_text)