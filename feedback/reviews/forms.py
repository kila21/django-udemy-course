
from django import forms 


class ReviewFrom(forms.Form):
    user_name = forms.CharField(label='Your Name', max_length=100, error_messages={
        'required': 'Your name must be not empty!',
        'max_length': 'Please enter a shorter name!'
    })
 