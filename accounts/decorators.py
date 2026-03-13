from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def role_required(*roles):
    def in_roles(user):
        if user.is_authenticated:
            if user.is_superuser or user.role in roles:
                return True
        raise PermissionDenied
    return user_passes_test(in_roles)
