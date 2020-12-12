from __future__ import absolute_import, unicode_literals
from celery import Celery


App = Celery('proj', backend='redis://:@127.0.0.1:6379/12',
             broker='redis://:@127.0.0.1:6379/11',
             include=["proj.tasks"])
App.config_from_object('proj.celeryconfig')

# Optional configuration, see the application user guide.
App.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    App.start()
