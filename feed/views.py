from django.shortcuts import render,redirect,resolve_url,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required

from common.models import User
from .forms import *
from .models import *
from chat.filtering import classify_sentence

# Create your views here.
@login_required(login_url='/common/login/')
def feed(request,user_nickname):
    user = User.objects.all().filter(nickname=user_nickname)
    afeed = artistfeed.objects.all().filter(author = user[0].id).order_by('-create_date')
    ufeed = userfeed.objects.all().filter(feedroom = user_nickname).order_by('-create_date')
    if request.method == 'POST' and 'userfeed' in request.POST:
        form = userfeedform(request.POST)
        if form.is_valid():
            vil = classify_sentence(request.POST['post'])
            ufeedform = form.save(commit=False)
            ufeedform.feedroom = user_nickname
            ufeedform.author = request.user
            ufeedform.create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ufeedform.vilification = vil
            ufeedform.save()
            data = {'message': str(int(vil))}
            return redirect('/feed/'+user_nickname+'/?message='+str(int(vil)),user_nickname)
    elif request.method == 'POST' and 'artistfeed' in request.POST:
        form = artistfeedform(request.POST)
        if form.is_valid():
            afeedform = form.save(commit=False)
            afeedform.author = request.user
            afeedform.create_date = datetime.now()
            afeedform.save()
            return redirect('feed:feed',user_nickname)
    else:
        ufeedform = userfeedform()
        afeedform = artistfeedform()
    context = {'user':user[0],'ufeedform':ufeedform,'afeedform':afeedform,'userfeed':ufeed,'artistfeed':afeed,'user_nickname':user_nickname}
    return render(request, 'feed/feed.html',context)

def ufeed_delete(request,ufeed_id):
    ufeed = get_object_or_404(userfeed, pk=ufeed_id)
    if request.user != ufeed.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        ufeed.delete()
    return redirect('feed:feed', user_nickname=ufeed.feedroom)

def afeed_delete(request,afeed_id):
    afeed = get_object_or_404(artistfeed, pk=afeed_id)
    user = User.objects.all().filter(nickname=afeed.author)[0]
    print('afeed : ',afeed)
    print('user : ',user)
    if request.user != afeed.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        afeed.delete()
    return redirect('feed:feed', user_nickname=user.nickname)