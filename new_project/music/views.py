from django.http import Http404
from .models import Album
from django.shortcuts import render

# Create your views here.
def index(request):
   data=Album.objects.all()
   return  render(request,'music/index.html', {'data' : data })
   
def details(request,album_id):
    try:
       data=Album.objects.get(pk=album_id)
    except Album.DoesNotExists:
        raise Http404('Album does not exist')
    return  render(request,'music/details.html', {'data':data}) 