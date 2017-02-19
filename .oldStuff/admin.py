from behave import *
from django.contrib.auth.models import User

# from bdd.factories import AdminFactory

use_step_matcher("re")


@given('I am an Administrator')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    # Creates a dummy admin user for tests
    '''
    a = AdminFactory(username='testAdmin', email='testing@tutrapp.com')
    a.set_password('password')

    # Don't omit to call save() to insert object in database
    a.save()
    '''
    context.user = User.objects.create_user(
        username='admintesting',
        email='admintesting@tutrapp.com',
        password='password'
    )
    assert (context.user.username == 'admintesting')


@given('I access the URL "/admin"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I see the admin login")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I submit a valid Administrator Account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    br.get(context.base_url + '/admin/login/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('testAdmin')
    br.find_element_by_name('password').send_keys('password')
    br.find_element_by_name('submit').click()


@then('Login is Success')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    assert br.current_url.endswith('/admin/')
    assert br.find_element_by_id('site-name').text == 'Django administration'


@step("I enter an INVALID Administrator Account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('DIV ID="Content" should contain P CLASS="errornote"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('contain text="Please enter the correct username and password for a staff account"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
