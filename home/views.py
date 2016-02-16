from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Store

class IndexView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'stores'

	def get_queryset(self):
		return Store.objects.order_by('-created')[:5]

class DetailView(generic.DetailView):
	model = Store
	template_name = 'home/detail.html'
	