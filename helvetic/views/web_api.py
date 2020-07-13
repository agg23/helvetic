# -*- mode: python; indent-tabs-mode: nil; tab-width: 2 -*-
"""
web_api.py - API to consume / update records
"""
from __future__ import absolute_import

from django.contrib.auth.models import User
from django.core import serializers
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from ..models import Measurement

class MeasurementListView(ListView):
  @method_decorator(csrf_exempt)
	@method_decorator(transaction.atomic)
	def dispatch(self, *args, **kwargs):
		return super(MeasurementListView, self).dispatch(*args, **kwargs)

  def get_queryset(self):
    user = User.objects.get(id=self.kwargs.get('pk'))
    return Measurement.objects.filter(user=user,synced_to_hk=False)

  def render_to_response(self, context):
    data = serializers.serialize('json', self.get_queryset())
    return HttpResponse(data, content_type='application/json')


class MeasurementView(UpdateView):
  model = Measurement
  fields = ['synced_to_hk']

  @method_decorator(csrf_exempt)
	@method_decorator(transaction.atomic)
	def dispatch(self, *args, **kwargs):
		return super(MeasurementView, self).dispatch(*args, **kwargs)
    
  def form_valid(self, form):
    self.object.synced_to_hk = self.request.POST.get('synced_to_hk') == 'true'
    self.object.save()
    return self.render_to_response(self.get_context_data())

  def render_to_response(self, context):
    data = serializers.serialize('json', [self.get_object()])
    return HttpResponse(data, content_type='application/json')