from django.db import models
from common.models import User

# Create your models here.

class artistfeed(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_artist',null=False)
    post = models.CharField(max_length=128,null=False)
    create_date = models.DateTimeField()
    vilification = models.BooleanField(default=False)
    
class userfeed(models.Model):
    feedroom = models.CharField(max_length=128,null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_user',null=False)
    post = models.CharField(max_length=128,null=False)
    create_date = models.DateTimeField()
    vilification = models.BooleanField(default=False)