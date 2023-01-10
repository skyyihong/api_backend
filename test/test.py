import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_backend.settings')
django.setup()

# 项目和django其他的包要在以上命令之后引入
from user.models import User

# print(Student)
if __name__ == '__main__':
    user = User.objects.all().first()
    print(user.check_password("1233"))
