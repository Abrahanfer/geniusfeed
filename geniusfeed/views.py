from rest_framework import permissions, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from geniusfeed.models import Feed, FeedItem, FeedItemRead
from geniusfeed.serializers import FeedSerializer, UserSerializer
from geniusfeed.serializers import FeedItemSerializer, FeedItemReadSerializer
from django.contrib.auth.models import User
from geniusfeed.permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


#@permission_classes((permissions.AllowAny,))
class FeedViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        feed = serializer.save()
        feed.users.add(self.request.user)

class FeedItemViewSet(viewsets.ModelViewSet):
    queryset = FeedItem.objects.all()
    serializer_class = FeedItemSerializer
    permissions_class = (permissions.IsAuthenticatedOrReadOnly,)



class FeedItemReadViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FeedItemRead.objects.all()
    serializer_class = FeedItemReadSerializer
    permissions_class = (IsOwner,)

    def perform_create(self, serializer):
        feeditemread = serializer.save()
        feeditemread.user = self.request.user


@permission_classes((permissions.AllowAny,))
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
