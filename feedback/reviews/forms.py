
from django import forms 


class ReviewFrom(forms.Form):
    user_name = forms.CharField()