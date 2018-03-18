from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import RestaurantLocation

def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
				"objectList":queryset,
				}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	context_object_name = 'objectList'
	template_name = 'restaurants/restaurants_list.html'
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(Q(category__iexact = slug)|Q(category__icontains = slug))
		else:
			queryset = RestaurantLocation.objects.all()	
		return queryset	

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()
	context_object_name = 'obj'

	def get_object(self, *args, **kwargs):
		rest_id = self.kwargs.get('rest_id')
		obj = get_object_or_404(RestaurantLocation, id=rest_id)
		return obj
	#def get_context_data(self, *args, **kwargs):
	#	print(self.kwargs)
	#	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	#	print(context)
	#	return context

#class AmericanRestaurantListView(ListView):
#	queryset = RestaurantLocation.objects.filter(category__iexact='american')	
#	template_name = 'restaurants/restaurants_list.html'	


