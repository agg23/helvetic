# -*- mode: python; indent-tabs-mode: nil; tab-width: 2 -*-
from __future__ import absolute_import
from django.conf.urls import include, url
from .views import aria_api, registration, webui, web_api

urlpatterns = [
  url(
    r'^scale/register$',
    aria_api.ScaleRegisterView.as_view(),
    name='scaleapi_register'
  ),

  url(
    r'^scale/upload$',
    aria_api.ScaleUploadView.as_view(),
    name='scaleapi_upload'
  ),

  url(
    r'^scale/validate$',
    aria_api.ScaleValidateView.as_view(),
    name='scaleapi_validate'
  ),
  
  url(
    r'^scales/$',
    webui.ScaleListView.as_view(),
    name='scale_list'
  ),
  
  url(
    r'^scales/register/$',
    registration.RegistrationView.as_view(),
    name='register_index'
  ),

  url(
    r'^scales/register/curl$',
    registration.CurlRegistrationView.as_view(),
    name='register_curl'
  ),

  url(
    r'^$',
    webui.IndexView.as_view(),
    name='index'
  ),

  url(
    r'^api/users/(?P<pk>[\d]+)/measurements/?$',
    web_api.MeasurementListView.as_view(),
    name='measurement_list'
  ),

  url(
    r'^api/measurements/(?P<pk>[\d]+)/?$',
    web_api.MeasurementView.as_view(),
    name='measurement'
  ),

  #url(r'^$', 'helvetic.views.home', name='home'),
]
