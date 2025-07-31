from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *

class artistfeedform(forms.ModelForm):
    class Meta:
        model = artistfeed
        fields = ['post']
        labels = {
            'post': _('내용')
        }
    
    
class userfeedform(forms.ModelForm):
    class Meta:
        model = userfeed
        fields = ['post']
        labels = {
            'post' : _('내용')
        }