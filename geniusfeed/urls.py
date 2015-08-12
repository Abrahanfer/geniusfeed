from django.conf.urls import patterns, include, url
from django.contrib import admin
#Using url like models?
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, renderers
from rest_framework.urlpatterns import format_suffix_patterns
#Custom views from geniusfeed
from geniusfeed import views
# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'feeds', views.FeedViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'feed_items', views.FeedItemViewSet)
router.register(r'feed_item_reads', views.FeedItemReadViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geniusfeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^feeds/$', feed_list, name='feed-list'),
    #url(r'^feeds/(?P<pk>[0-9]+)$', feed_detail, name='feed-details'),
    #url(r'^users/$', user_list, name='user-list'),
    #url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
)

#urlpatterns = format_suffix_patterns(urlpatterns)
