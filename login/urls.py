from django.urls import path, re_path
from login import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from utils.custom_verify_token import custom_verify_jwt_token
from utils.custom_get_token import custom_obtain_jwt_token

urlpatterns = [
    re_path('^get_token/', custom_obtain_jwt_token),  # 自定义方式,实现多账号登录方式
    re_path('^refresh_token/', refresh_jwt_token),
    re_path('^verify_token/', custom_verify_jwt_token),  # 自定义了token验证的返回值
]
