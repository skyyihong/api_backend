from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CustomJSONWebTokenSerializer(JSONWebTokenSerializer):

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            username = credentials.get("username")
            password = credentials.get("password")
            try:
                user_model = get_user_model()
                user = user_model.objects.get(
                    Q(username=username) | Q(mobile=username) | Q(email=username))  # 用户名 手机 邮箱任何一个符合即可
                user = user if user.check_password(raw_password=password) else None
            except user_model.DoesNotExist as e:
                user = None
            if user:
                if not user.is_active:
                    msg = '用户账号已禁用.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = '账号或密码错误'
                raise serializers.ValidationError(msg)
        else:
            msg = '登录必须包括认证账号和密码信息'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class CustomObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = CustomJSONWebTokenSerializer
    throttle_classes = []  # 该接口不做限流操作


custom_obtain_jwt_token = CustomObtainJSONWebToken.as_view()
