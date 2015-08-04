from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from geniusfeed.models import Feed, FeedItem
from geniusfeed.serializers import FeedSerializer

@api_view(['GET', 'POST'])
def feed_list(request):
    """
    List all feed, or create a new feed
    """
    if request.method == 'GET':
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = FeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def feed_details(request, pk):
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
