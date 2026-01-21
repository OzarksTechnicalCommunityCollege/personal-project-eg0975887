from django.shortcuts import get_object_or_404, render
from .models import VGForm
from django.http import Http404

# Create your views here.

def version_list(request): # View to list all of the written reviews
    versions = VGForm.objects.all()
    
    return render(
        request,
        'VGForum/version/list.html',
        {'versions': versions}
    )
    
def version_detail(request, pk): # View to show the details of a specific review
    versions = get_object_or_404(VGForm, pk=pk) # The review is sent to the detail view using its primary key from the list view
    return render(
        request, 
        'VGForum/version/detail.html',
        {'versions': versions}
    )