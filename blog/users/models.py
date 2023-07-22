from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.


class User(AbstractUser):


    #在继承django的User模型类中增加我们自己需要的字段

    # 增加手机号字段
    mobile = models.CharField(verbose_name="手机号",max_length=11,unique=True,blank=False)
    #增加签名字段
    sign = models.CharField(verbose_name='个人签名',blank=True,max_length=255)
    #增加头像字段
    img = models.ImageField(verbose_name='头像',upload_to=r'img/%Y%m%d/',blank=True)

    class Meta:
        db_table = 'blog_users'#修改表名
        verbose_name = '用户管理'#admin后台显示
        verbose_name_plural = verbose_name#后台复数显示

    def __str__(self) -> str:
        return self.mobile