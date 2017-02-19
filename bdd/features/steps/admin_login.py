from behave import *

use_step_matcher("re")


@given("I am an Admin User")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I log in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Login is a Success")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
