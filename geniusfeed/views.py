from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from geniusfeed.models import Feed, FeedItem
from geniusfeed.serializers import FeedSerializer

class JSONResponse(HttpResponse):
    """
    An HttpRepsonse that renders its content into JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def feed_list(request):
    """
    List all feed, or create a new feed
    """
    if request.method == 'GET':
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = FeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def feed_details(request, pk):
    """
    Return detail view for Feed
    """
    try:
        feed = Feed.objects.get(pk=pk)
    except Feed.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FeedSerializer(feed)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = FeedSerializer(feed, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        feed.delete()
        return HttpResponse(status=204)
