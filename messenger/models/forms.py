from .models import UserMessenger
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        UserMessenger.objects.create(user=user)
        return user
    
    class Meta:
        fields = '__all__'