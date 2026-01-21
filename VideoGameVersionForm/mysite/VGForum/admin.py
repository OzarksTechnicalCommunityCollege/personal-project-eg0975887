from django.contrib import admin
from .models import VGForm

# Register your models here.
@admin.register(VGForm)
class VGFormAdmin(admin.ModelAdmin):
    list_display = ('versionNum', 'created', 'completionStatus', 'additionalcomments') # Fields to display in the admin list view
    list_filter = ('completionStatus', 'created') # Filters for the admin list view
    search_fields = ('versionNum', 'additionalcomments') # Searchable fields in the admin interface
    show_facets = admin.ShowFacets.ALWAYS # This enables facets in the admin interface which displays the number of items in each filter category
    
