from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        #You could just use pass here, and the function would return None by default. However, because we specifically need the function to return None, the "explicit is better than implicit" rule applies here.
        except User.DoesNotExist:
            return None
