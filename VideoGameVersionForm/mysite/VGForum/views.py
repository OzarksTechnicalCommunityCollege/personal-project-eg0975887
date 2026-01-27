from django.shortcuts import get_object_or_404, render
from .models import VGForm
from .forms import VGFourmForm
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


def vg_create(request): # View to create a new VGForm entry
    if request.method == 'POST': # check to see if the page is pushing a form to be submitted 
        form = VGFourmForm(request.POST)
        if form.is_valid():
            vgform = form.save()
    else: # if the page is being loaded normally, create a blank form
        form = VGFourmForm()
        
    return render(
        request,
        'VGForum/version/create.html',
        {'form': form}
    )