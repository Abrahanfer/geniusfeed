from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.views import APIView
from geniusfeed.models import Feed, FeedItem
from geniusfeed.serializers import FeedSerializer

@permission_classes((permissions.AllowAny,))
class FeedList(APIView):
    """
    List all feed, or create a new feed
    """
    def get(self, request, format=None):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class FeedDetails(APIView):
    """
    Return detail view for Feed
    """
    def get_object(self, pk):
        try:
            feed = Feed.objects.get(pk=pk)
        except Feed.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        feed = self.get_object(pk)
        serializer = FeedSerializer(feed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        feed = self.get_object(pk)
        serializer = FeedSerializer(feed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        feed = self.get_object(pk)
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
