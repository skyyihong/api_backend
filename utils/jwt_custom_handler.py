def custom_jwt_response_payload_handler(token, user=None, request=None):
    '''
    自定义了jwt的返回值
    '''

    return {
        'id': user.id,
        'user': user.username,
        'nickname': user.first_name + user.last_name,
        'token': token,
    }
