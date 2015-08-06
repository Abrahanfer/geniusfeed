from django.forms import widgets
from rest_framework import serializers
from geniusfeed.models import Feed, FeedItem
from django.contrib.auth.models import User

class FeedSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=True, allow_blank=True, max_length=200)
    # link = serializers.URLField(required=True, max_length=200)

    # def create(self, validate_data):
    #     """
    #     Create and return a new Feed instance
    #     """
    #     return Feed.objects.create(**validate_data)

    # def update(self, validate_data):
    #     """
    #     Update a Feed instance with new validate_data
    #     """
    #     instance.title = validate_data.get('title', instance.title)
    #     instance.link = validate_data.get('link', instance.link)
    #     instance.save()

    #     return instance
    users = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = Feed
        fields = ('title', 'link', 'users')

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    feed_set = serializers.PrimaryKeyRelatedField(many=True, queryset='feed_set')

    class Meta:
        model = User
        fields = ('username', 'email', 'feed_set')
