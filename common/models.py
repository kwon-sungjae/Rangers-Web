from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.template.defaultfilters import slugify

# Create your models here.
class UserManager(BaseUserManager):    
    def create_user(self, email, nickname, password=None):        
        if not email :            
            raise ValueError('이메일을 입력해주세요.')
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user  
       
    def create_superuser(self, email, nickname, password):        
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user
    
def image_upload_path(instance, filename):
    username = instance.nickname
    return "img/user/%s/%s" % (username, filename)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True) # 로그인용 아이디
    name = models.CharField(max_length=10,null=False) # 이름
    nickname = models.CharField(max_length=20,null=False,unique=True) # 닉네임
    is_active = models.BooleanField(default=True) # 로그인 가능한가? (벤여부)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True) # 생성일자
    profileimage = models.ImageField(upload_to=image_upload_path,null=True,blank=True,default='img/baseimage.jpg')
    is_artist = models.BooleanField(default=False)           
    is_live = models.BooleanField(default=False)
    agency = models.CharField(max_length=100,null=True,blank=True) # 소속사
    artistgroup = models.CharField(max_length=100,null=True,blank=True)
    counting = models.IntegerField(default=500)

    objects = UserManager()
    USERNAME_FIELD = 'email' # 로그인용  
    EMAIL_FIELD = "email"  
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname
    
    class Meta:
        db_table = 'User'