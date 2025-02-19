from django_filters import FilterSet
from .models import UserMessenger

class UserFilter(FilterSet):

    class Meta:
        model = UserMessenger
        fields = {
            'user__username':['icontains']
        }

        