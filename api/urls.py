
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # re_path('^messages/(?P<sender>.+)/$', views.MessageNewViewSet),
]
urlpatterns = format_suffix_patterns(urlpatterns)