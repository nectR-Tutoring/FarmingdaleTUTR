from django.template.defaultfilters import slugify
from factory import DjangoModelFactory, lazy_attribute
from factory import PostGenerationMethodCall
from faker import Factory

fake = Factory.create()


class User(DjangoModelFactory):
    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username',)

    first_name = lazy_attribute(lambda o: fake.first_name())
    last_name = lazy_attribute(lambda o: fake.last_name())
    username = lazy_attribute(lambda o: slugify(o.first_name + '.' + o.last_name))
    email = lazy_attribute(lambda o: o.username + "@example.com")
    password = PostGenerationMethodCall('set_password', 'passw0rd')

    is_superuser = False
    is_staff = False
    is_active = True
