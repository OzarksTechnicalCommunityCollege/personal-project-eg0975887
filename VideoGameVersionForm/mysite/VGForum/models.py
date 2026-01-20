from django.db import models
from django.utils import timezone

# Create your models here.

class VGForm(models.Model):

    class CompletionStatus(models.TextChoices):
        NONE = 'ND', 'No Dungeon'
        FIRST = 'FD', 'First Dungeon'
        SECOND = 'SD', 'Second Dungeon'
        THIRD = 'TD', 'Third Dungeon'


    versionNum = models.CharField(max_length=250)
    created = model.DatetimeField(auto_now_add=True)
    completionStatus = models.CharField(
        max_length=4,
        choices=CompletionStatus,
        default=CompletionStatus.NONE
    )
    additionalcomments = models.TextField()

def __str__(self):
    return self.title
    

