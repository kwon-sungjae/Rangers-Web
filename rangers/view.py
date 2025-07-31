from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from common.models import User
from django.db.models import Q

# Create your views here. -----------------------------------------------------------------------
def home(request):
    userlist = User.objects.all().filter(is_artist=1)

    kw = request.GET.get('kw','') # 검색어
    if kw:
        userlist = userlist.filter(
            Q(nickname__icontains=kw) |
            Q(name__icontains=kw) |
            Q(agency__icontains=kw) |
            Q(artistgroup__icontains=kw)
        ).distinct()
        
    return render(request, 'main/mainpage.html',{'userlist':userlist})