from django.utils.timezone import now
from mentor.models import User


class UserBackend(object):
    """
    Authenticates a user against mentor.models.User
    """
    supports_inactive_user = False

    def authenticate(self, email=None, password=None):
        if email is None: return None
        try:
            user = User.objects.get(email=email.lower())
            if user.check_password(password):
                return user
        except User.DoesNotExist: # user does not exist
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
