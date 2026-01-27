from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class UniversalModel(models.Model): # Class for inheriting field for all models (and to help reduce size of models for better readability)
    created = models.DateTimeField(auto_now_add=True) # When the review was created

    # Use Meta class to make this an abstract model (not a database table)
    class Meta:
        abstract = True


class VGForm(UniversalModel):

    # This class holds all the choices for the completion status field
    class CompletionStatus(models.TextChoices):
        NONE = 'ND', 'No Dungeon'
        FIRST = 'FD', 'First Dungeon'
        SECOND = 'SD', 'Second Dungeon'
        THIRD = 'TD', 'Third Dungeon'

    versionNum = models.CharField(max_length=250) # Variable of what version of the game is being documented
    
    completionStatus = models.CharField( # Level of completion from the reviewer
        max_length=4,
        choices=CompletionStatus,
        default=CompletionStatus.NONE
    )
    
    additionalcomments = models.TextField() # Additional comments from the reviewer

def __str__(self):
    return self.versionNum

    

