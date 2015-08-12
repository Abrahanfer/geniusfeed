from rest_framework import permissions, generics, viewsets
from rest_framework.decorators import list_route, permission_classes
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
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FeedItem.objects.all()
    serializer_class = FeedItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                         IsOwnerOrReadOnly)


class FeedItemReadViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = FeedItemReadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return FeedItemRead.objects.filter(user=self.request.user.pk)

    def perform_create(self, serializer):
        feeditemread = serializer.save()
        feeditemread.user = self.request.user

    #Get unread feedItems
    @list_route()
    def unread(self, request):
        unread_feed_items = FeedItemRead.objects.filter(user=self.request.user.pk).exclude(read=True)

        page = self.paginate_queryset(unread_feed_items)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(unread_feed_items, many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
