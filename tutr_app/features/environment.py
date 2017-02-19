import django
import os
from splinter.browser import Browser

# This is necessary for all installed apps to be recognized, for some reason.
os.environ['DJANGO_SETTINGS_MODULE'] = 'tutr_app.settings.dev'

# Setup Django
django.setup()


def before_all(context):
    # PhantomJS is used there (headless browser)
    # For debugging purposes, you can use the Firefox driver instead.

    context.browser = Browser('phantomjs')
    context.server_url = 'http://localhost:8000'


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass
