BROKER_URL = 'redis://localhost:6379/10'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/11'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
        'task_cron_job_10_sec': {
            'task': 'proj.tasks.celery_test_print',
            'schedule': 10,
        },
}
