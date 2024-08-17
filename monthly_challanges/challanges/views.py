from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.template.loader import render_to_string


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
def index(request):
    list_items = ''
    months = list(monthly_challanges.keys())
    
    for month in months:
        capitalized = month.capitalize()
        list_items += f'<li><a href="{month}">{capitalized}</a></li>'

    response = f"""
        <ul>
        {list_items}
        </ul>
    """
    return HttpResponse(response)

def monthly_challange_by_number(request, month):
    months = list(monthly_challanges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid Month')
    redirect_month = months[month-1]
    return HttpResponseRedirect(redirect_month)

def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]

         # return HttpResponse(challange_text)
        return render(request, 'challanges/challange.html', {"text": challange_text, "month_name": month})
         
        # return HttpResponse(render_to_string('challanges/challange.html'))
    except:
        return HttpResponseNotFound('Month isnt Supported!')
        # return render(request, 'challanges.html')
    
   