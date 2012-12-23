from fabric.api import * # importing: local, settings,abort, run, cd, env
from fabric.contrib.console import confirm
import os
import sys

PROJECT_FULL_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
sys.path.append(PROJECT_FULL_PATH)

myproject = PROJECT_FULL_PATH.split('/')[-1] + ".settings"
myproject = __import__(myproject)
INSTALLED_APPS = ( app for app in  myproject.settings.INSTALLED_APPS if not "django" in app )

def runserver():
    local('python manage.py runserver')

def validate():
    local('python manage.py validate')

def update_db():
    print '\n=========SYNC========\n'
    local('python manage.py syncdb')
    print '\n=========SQL=========\n'
    for app in INSTALLED_APPS:
        local('\n\npython manage.py sqlall %s' %app)

def test():
    for app in INSTALLED_APPS:
        with settings(warn_only=True):
            result = local('\n\npython manage.py test %s' %app, capture=False)
            if not result.failed:
                print "\033[0;32mPASS\n\033[0m"
            elif result.failed and not confirm('Tests failed. Continue anyway?'):
                abort('Aborting at user request.')
                break

def commit():
    local('git add * && git commit')

def push():
    local('git push')

def prepare_deploy():
    test()
    commit()
    push()

def host_type():
    run('uname -s')   
