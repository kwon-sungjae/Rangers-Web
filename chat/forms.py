from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat # 사용할 모델
        fields = ['id','author','message','create_date','vilification'] # 폼에서 사용할 모델의 속성 
        # form 이름 지정
        labels = {
            'id': _('방번호'),
            'author':_('작성자'),
            'message':_('내용'),
            'create_date':_('작성시간'),
            'vilification':_('비속어 판별'),
        }
        