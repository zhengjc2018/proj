from __future__ import absolute_import
from proj.app import App


@App.task(name="celery_test_print")
def celery_test_print():
    print("celery_test_print")
