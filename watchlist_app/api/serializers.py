from rest_framework import serializers
from watchlist_app.models import *

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['watchlist']
        #fields = "__all__"

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

    reviews = ReviewSerializer(many=True, read_only=True)
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and description should be different")
        else:
            return data
        
    def validate_description(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Description is too short!")
        else:
            return value

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title is too short!")
        else:
            return value
        
    def validate(self, data):
        request = self.context['request']
        watchlist_id = self.context['view'].kwargs.get('pk')

        if Review.objects.filter(
            watchlist_id=watchlist_id,
            review_user=request.user
        ).exists():
            raise serializers.ValidationError("Already reviewed")
        else:
            return data
        


class StreamPlatformSerializer(serializers.ModelSerializer):
    #We did pass streamPlatform.objects.all() as an arguement to the serializer in views.py
    #It contains related name but it's not visisble in the models.py
    #(related_name='watchlist') is a distinct field, we use it to relate to another table
    #watchlist = WatchlistSerializer(many=True, read_only=True)
   
    watchlist = WatchlistSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"



# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is to short")
    
# class MovieSerializer(serializers.Serializer):
#     #get here
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     #Post and Put here
#     def create(self, validated_data):
#         #We need to validate the data to ensure that name, description and is active is entered 
#         return Movie.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         #instance carry the old values
#         #validate_data data contains the new values
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.name)
#         instance.active = validated_data.get('active', instance.active)        
#         instance. save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should be different")
#         else:
#             return data
    
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is to short!")
#     #     else:
#     #         return value
