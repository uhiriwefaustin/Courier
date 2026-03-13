import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courier_system.settings')
django.setup()

from accounts.models import User

username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password, role='Admin')
    print(f"Superuser '{username}' created successfully.")
else:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print(f"Superuser '{username}' password updated.")
