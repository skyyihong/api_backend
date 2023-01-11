from rest_framework_jwt.views import VerifyJSONWebToken
from rest_framework.response import Response
import datetime
from rest_framework_jwt.settings import api_settings
from rest_framework import status

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class CustomVerifyJSONWebToken(VerifyJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response({"code": True}, status=status.HTTP_200_OK)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response({"code": False}, status=status.HTTP_400_BAD_REQUEST)


custom_verify_jwt_token = CustomVerifyJSONWebToken.as_view()
