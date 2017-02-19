import factory
import factory.django
from django.contrib.auth.models import User


class AdminFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = 'TestAdmin'
    email = 'test@tutrapp.com'
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

    is_superuser = True
    is_staff = True
    is_active = True
