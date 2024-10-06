
from django import forms 
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your Name', max_length=100, error_messages={
#         'required': 'Your name must be not empty!',
#         'max_length': 'Please enter a shorter name!'
#     })
#     review_text = forms.CharField(label='Your Feedback', max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['user_name']