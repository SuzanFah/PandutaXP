from django.contrib.auth.backends import ModelBackend

class CustomAuthBackend(ModelBackend):
    def get_user_redirect_url(self, user):
        if hasattr(user, 'provider'):
            return 'providers_dashboard'
        return 'clients_dashboard'
