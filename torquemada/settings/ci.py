from .base import *


INSTALLED_APPS = INSTALLED_APPS + ('django_jenkins',)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
)