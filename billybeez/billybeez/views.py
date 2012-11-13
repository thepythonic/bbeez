from django.conf import settings
from django.shortcuts import render_to_response

def billybeez_404_view(request):
	return render_to_response('404-error.html')

def billybeez_500_view(request):
	return render_to_response('500-error.html')