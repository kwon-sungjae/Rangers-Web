from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('<str:user_nickname>/',views.feed,name='feed'),
    path('udelete/<int:ufeed_id>',views.ufeed_delete,name='ufeed_delete'),
    path('adelete/<int:afeed_id>',views.afeed_delete,name='afeed_delete'),
]    