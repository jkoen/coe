from django.conf.urls import url

import views


urlpatterns = [
    url(
        r'offering_request/$',
        views.offering_request,
        name='offering_request',
    ),
    url(
        r'platform/(?P<pk>\d+)/configuration/$',
        views.PlatformConfiguration.as_view(),
        name='platform_configuration',
    ),
    url(
        r'platform/(?P<platform_pk>\w+)/offering/(?P<offering_pk>\w+)/configuration/$',
        views.PlatformOfferingConfiguration.as_view(),
        name='platformoffering_configuration',
    ),
    url(
        r'thanks/$',
        views.thanks,
        name='thanks',
    ),
]

