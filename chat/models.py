from django.db import models

# Create your models here.
from django.db import models
from common.models import User

# Create your models here.

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    roomname = models.CharField(max_length=30,null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='chat_author',null=False)
    message = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)
    vilification = models.BooleanField(default=False)

    class Meta:
        db_table = 'chat'

    def __str__(self):
        return str(self.id)