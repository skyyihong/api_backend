import os
import django
from rest_framework.settings import api_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_backend.settings')
django.setup()

# 项目和django其他的包要在以上命令之后引入
from user.models import User
from django.core.cache import caches, cache
import time

# print(Student)
if __name__ == '__main__':
    # cache.set("name1", "hongyan", 60 * 60)
    # time.sleep(1)
    n = cache.get("name1")
    print(n)
    THROTTLE_RATES = api_settings.DEFAULT_PAGINATION_CLASS
    print(THROTTLE_RATES)
