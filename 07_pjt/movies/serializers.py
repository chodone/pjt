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
