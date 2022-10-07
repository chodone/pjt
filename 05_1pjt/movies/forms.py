
from django import forms
from .models import Movie
from django.forms.widgets import NumberInput


class MovieForm(forms.ModelForm):

    GENRE_CHOICES = [
        ('코미디', '코미디'),
        ('공포', '공포'),
        ('로맨스', '로맨스')

    ]
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    score = forms.FloatField(widget=forms.NumberInput(attrs=({'step' : 0.5 , 'min' : 0, 'max' : 5})))
    release_date = forms.DateField(widget=NumberInput(attrs={'type' : 'date'}))
    

    class Meta:
        model = Movie
        fields = '__all__'
