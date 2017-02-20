from behave import given, when, then, use_step_matcher, step

from tutr_app.factories.user import User

use_step_matcher("parse")


@given("I am an Administrator")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_admin_user = User(is_superuser=True)
    assert context.test_admin_user.is_superuser


@step(u'I am using server "{url}"')
def step_impl(context, url):
    """
    :param url:
    :type context: behave.runner.Context
    """
    context.config.server_url = url


@when('I visit "{login_page}"')
def step_impl(context, login_page):
    """
    :param login_page: /admin/
    :type context: behave.runner.Context
    """
    context.browser.visit(context.config.server_url + login_page)



@step("I enter Administrator Username and Password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Login is Success")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I am redirected to Admin Backend")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
