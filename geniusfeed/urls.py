from django.conf.urls import patterns, include, url
from django.contrib import admin
#Using url like models?
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
#Custom views from geniusfeed
from geniusfeed import views

# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geniusfeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^feeds/$', views.FeedList.as_view()),
    url(r'^feeds/(?P<pk>[0-9]+)$', views.FeedDetails.as_view()),
  #  url(r'^', include(router.urls)),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns = format_suffix_patterns(urlpatterns)
