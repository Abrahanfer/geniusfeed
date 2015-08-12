from django.forms import widgets
from rest_framework import serializers
from geniusfeed.models import Feed, FeedItem, FeedItemRead
from django.contrib.auth.models import User

class FeedSerializer(serializers.HyperlinkedModelSerializer):
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
        #users = serializers.ReadOnlyField()

    feed_items = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='feeditem-detail')

    class Meta:
        model = Feed
        fields = ('pk', 'title', 'link', 'feed_items')

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    feed_set = serializers.HyperlinkedRelatedField(many=True, view_name='feed-detail', read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'feed_set')

class FeedItemSerializer(serializers.HyperlinkedModelSerializer):
    #feeditemread_set = FeedItemReadSerializer(many=True)
    feed = serializers.PrimaryKeyRelatedField(queryset='feed')


    class Meta:
        model = FeedItem
        fields = ('pk', 'title', 'link', 'feed')

class FeedItemReadSerializer(serializers.ModelSerializer):
    feed_item = FeedItemSerializer(read_only=True)

    class Meta:
        model = FeedItemRead
        fields = ('pk', 'update_date', 'read', 'fav', 'feed_item')
        read_only_fields = ('feed_item',)
