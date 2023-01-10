from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    '''
    自定义基础字段做为基类
    '''
    creat_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True


class UserInfo(BaseModel):
    address = models.CharField(max_length=256, null=True, )
    user = models.OneToOneField(to="User", on_delete=models.DO_NOTHING, db_constraint=False)
    class Meta:
        db_table = "userinfo"


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    mobile = models.CharField(max_length=11, unique=True, null=True, blank=True, db_index=True, verbose_name="手机号码")
    oauth = models.CharField(max_length=256, verbose_name="第三方认证")
    creat_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")


    class Meta(AbstractUser.Meta):
        db_table = "user"
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name