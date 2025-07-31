from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreationForm(forms.ModelForm):
    # name = forms.CharField(label='*이름', max_length=10) # 이름
    password1 = forms.CharField(label='*비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='*비밀번호 확인', widget=forms.PasswordInput)
    # is_artist = forms.BooleanField(label='연예인 확인')
    # agency = forms.CharField(label='소속사', max_length=100) # 소속사
    # artistgroup = forms.CharField(label='그룹', max_length=100)
    profileimage = forms.ImageField(required=False)
    

    class Meta:
        model = User
        fields = ['name', 'email', 'nickname', 'is_admin','is_superuser','is_staff', 'is_artist', 'agency', 'artistgroup','profileimage',]
        labels = {
            'name' : _('*이름'),
            'email' : _('*아이디(이메일)'),
            'nickname' : _('*닉네임'),
            'is_admin' : _('admin'),
            'is_superuser' : _('슈퍼유저'),
            'is_staff' : _('스태프'),
            'is_artist' : _('연예인 확인'),
            'agency' : _('소속사'),
            'artistgroup' : _('소속그룹'),
            'profileimage' : _('프로필이미지'),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 서로 다릅니다")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        image = self.cleaned_data.get('profileimage')
        if image:
            user.profileimage = image
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['name', 'email', 'nickname', 'is_admin','is_superuser','is_staff', 'is_artist', 'agency', 'artistgroup', 'profileimage',]
        labels = {
            'name' : _('*이름'),
            'email' : _('*아이디(이메일)'),
            'nickname' : _('*닉네임'),
            'is_admin' : _('admin'),
            'is_superuser' : _('슈퍼유저'),
            'is_staff' : _('스태프'),
            'is_artist' : _('연예인 확인'),
            'agency' : _('소속사'),
            'artistgroup' : _('소속그룹'),
            'profileimage' : _('프로필이미지'),
        }
    

    def clean_password(self):
        return self.initial["password"]