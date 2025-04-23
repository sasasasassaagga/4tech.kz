from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "image", "first_name", "last_name", "email")


class CustomLoginView(LoginView):
    template_name = 'your_login_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_urls'] = ['login', 'signup', 'password_reset']  # Добавляем нужные URL names
        return context