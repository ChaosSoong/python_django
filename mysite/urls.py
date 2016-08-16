"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from mysite.views import hello,current_datetime,hours_ahead,display_meta,archive,dance
from django.contrib import admin
from books.views import search,search_form
from contact import views
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite import settings
admin.autodiscover()
urlpatterns = patterns('',
    ('^$', hello),
	(r'^admin/', include(admin.site.urls)),
	('^time/$',current_datetime),
	(r'^time/(\d{1,2})/$', hours_ahead),
	('^meta/$',display_meta),
	('^metas/$',archive),
	(r'^search-form/$', search_form),
	(r'^search/$', search),
	(r'^contact/$', views.contact),
	url(r'^dance/$', dance),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
