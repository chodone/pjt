# 07_pjt - DB 설계를 활용한 REST API 설계

## models.py 설계
```py
from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
```

- models.py 설계를 할때 요구사항의 ERD 뿐만 아니라 fixtures의 json파일의 구조에 따라 설계를 진행해야 한다는 것을 깨달았습니다. 


## serializer.py 설계
```py
from dataclasses import field
from rest_framework import serializers
from .models import Movie, Actor, Review

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)



class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content',)



class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)



class MovieTitle(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    movie = MovieTitle(read_only=True)
        



class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        
    class Actors(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('name',)


    class ReviewSet(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('title', 'content',)
    
    

    review_set = ReviewSet(many=True, read_only=True)
    actors = Actors(many=True, read_only=True)




class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
    
    
    movies = MovieTitle(many=True, read_only=True)        

```
- 출력하고 싶은 형태의 데이터가 있다면 새로운 class를 생성하여 사용하는 방법을 배웠습니다. 이때 만약 하나의 Aclass에서만 사용한다면 Aclass 안에서 생성하여 사용하고 여러 class에서 사용된다면 밖에다 생성하여 사용하는것이 올바른 구조인것 같습니다.



