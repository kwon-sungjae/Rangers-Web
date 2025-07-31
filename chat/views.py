from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from chat.models import Chat
from common.models import User

# Create your views here.

def chathome(request):
    userlist = User.objects.all().filter(is_artist=1)

    kw = request.GET.get('kw','') # 검색어
    if kw:
        userlist = userlist.filter(
            Q(nickname__icontains=kw) |
            Q(name__icontains=kw) |
            Q(agency__icontains=kw) |
            Q(artistgroup__icontains=kw)
        ).distinct()
        
    return render(request,'chat/chat.html',{'userlist':userlist})

@login_required(login_url='/common/login/')
def room(request, room_name):
    chatlist = Chat.objects.all().filter(roomname=room_name).order_by('create_date')
    user = request.user
    counting = user.counting/10
    userlist = User.objects.all().filter(is_artist=1)

    kw = request.GET.get('kw','') # 검색어
    if kw:
        userlist = userlist.filter(
            Q(nickname__icontains=kw) |
            Q(name__icontains=kw) |
            Q(agency__icontains=kw) |
            Q(artistgroup__icontains=kw)
        ).distinct()
    
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'request':request,
        'chatlist':chatlist,
        'counting':counting,
        'userlist':userlist,
        'room_name':room_name,
    })