import jwt

from my_settings import SECRET_KEY

def jwt_expression(func):
    def wrap(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)


        except:

            return access_token

        return func(*args, **kwargs)

    return wrap