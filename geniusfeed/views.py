from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from geniusfeed.models import Feed, FeedItem
from geniusfeed.serializers import FeedSerializer, UserSerializer
from django.contrib.auth.models import User
from geniusfeed.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'feeds': reverse('feed-list', request=request, format=format)
    })


#@permission_classes((permissions.AllowAny,))
class FeedList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def perform_create(self, serializer):
        feed = serializer.save()
        feed.users.add(self.request.user)


#@permission_classes((permissions.AllowAny,))
class FeedDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

@permission_classes((permissions.AllowAny,))
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes((permissions.AllowAny,))
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
