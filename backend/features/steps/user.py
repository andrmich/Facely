from behave import *
from django.contrib.auth.models import User

use_step_matcher("re")


@given("user with email 'user@example\.com' with password 'pass' exists")
def step_impl(context):
    assert User.objects.count() == 0
    User.objects.create_user(username='whatever', email='user@example.com', password='pass')
    assert User.objects.count() == 1


@when("user visits the log in page")
def step_impl(context):
    raise NotImplementedError(u'STEP: When user visits the log in page')


@then("a form asking for email and password displays")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a form asking for email and password displays')


@step("no username is displayed in login form")
def step_impl(context):
    raise NotImplementedError(u'STEP: And no username is displayed in login form')


@step("user can log in")
def step_impl(context):
    raise NotImplementedError(u'STEP: And user can log in')


@step("user is redirected to home page")
def step_impl(context):
    raise NotImplementedError(u'STEP: And user is redirected to home page')


@when("user visits the log out page")
def step_impl(context):
    raise NotImplementedError(u'STEP: When user visits the log out page')


@then("user can log out")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user can log out')


@step("user is redirected to log in page")
def step_impl(context):
    raise NotImplementedError(u'STEP: And user is redirected to log in page')


@step("user is logged in")
def step_impl(context):
    raise NotImplementedError(u'STEP: And user is logged in')


@step("user navigates to main page")
def step_impl(context):
    raise NotImplementedError(u'STEP: And user navigates to main page')


@then("user sees home page")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user sees home page')