from django import forms
from .models import VGForm


class VGFourmForm(forms.ModelForm): # django will pull from the ModelForm import to create a form based on the VGForm model
    class Meta:
        model = VGForm
        fields = ['completionStatus', 
                  'versionNum',
                  'additionalcomments'
        ]

        # NOTE: need to find a way to display the Text for the forms instead of pulling from the fields above