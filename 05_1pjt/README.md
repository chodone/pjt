# 05_pjt

 
```py
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

```

```html
<h1>CREATE</h1>
    <div>
    
        <form action="{% url 'movies:create' %}" method="post" class="form">
            {% csrf_token %}
            {% bootstrap_form form %}
            {% buttons %}
            <button type="submit" class="btn btn-primary">
                Submit
            </button>
        
            {% endbuttons %}
        </form>
    </div>
    <hr>
```
- forms.py에서 genre, score, release_date의 widget을 활용해서 수정하는데 어려움을 겪었다. 그러고 난 후 django-bootstrap을 적용하는 새로운 방법을 적용해 보았다.

- 전체적으로 django의 흐름과 css를 적용하는 방법이 많이 미숙하다고 느껴졌다. 
