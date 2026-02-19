from django.shortcuts import get_object_or_404, render
from .models import VGForm
from django.contrib.postgres.search import SearchVector
from .forms import VGFourmForm, SearchForm
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
    
def post_search(request): # View to handle searching through the reviews
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET: # Check to see if there is a search query
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = VGForm.objects.annotate(
                search=SearchVector('versionNum', 'additionalcomments', 'tags__name'),
            ).filter(search=query)
    
    return render(
        request,
        'VGForum/version/search.html',
        {'form': form,
         'query': query,
         'results': results}
    )