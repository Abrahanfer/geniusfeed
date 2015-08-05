from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from geniusfeed.models import Feed, FeedItem
from geniusfeed.serializers import FeedSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def feed_list(request, format=None):
    """
    List all feed, or create a new feed
    """
    if request.method == 'GET':
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def feed_details(request, pk, format=None):
    """
    Return detail view for Feed
    """
    try:
        feed = Feed.objects.get(pk=pk)
    except Feed.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = FeedSerializer(feed)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeedSerializer(feed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
