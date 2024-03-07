
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

class RegisterUserView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginUserView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
    
    
    
    
from django.contrib.auth import logout
from django.views.generic import RedirectView

from django.contrib.auth import logout  # Import the logout function

class LogoutView(RedirectView):
    url = '/login/'  # Redirect to login page after logout

    def get(self, request, *args, **kwargs):
        logout(request)  # Call the logout function
        return super().get(request, *args, **kwargs)