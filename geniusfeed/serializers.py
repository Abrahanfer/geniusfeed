from django.forms import widgets
from rest_framework import serializers
from geniusfeed.models import Feed, FeedItem

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

    class Meta:
        model = Feed
        fields = ('title', 'link')
