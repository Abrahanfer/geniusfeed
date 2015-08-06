from rest_framework import permissions, generics
from geniusfeed.models import Feed, FeedItem
from geniusfeed.serializers import FeedSerializer


@permission_classes((permissions.AllowAny,))
class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


@permission_classes((permissions.AllowAny,))
class FeedDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
