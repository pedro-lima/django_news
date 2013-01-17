from fabric.api import * # importing: local, settings,abort, run, cd, env
from fabric.contrib.console import confirm
from fabsettings import *
import os

def runserver():
    local('python manage.py runserver')

def validate():
    local('python manage.py validate')

def update_db():
    print '\n=========SYNC========\n'
    local('python manage.py syncdb')
    print '\n=========SQL=========\n'
    for app in INSTALLED_APPS:
        with settings(warn_only=True):
            result = local('\n\npython manage.py sqlall %s' %app, capture=False)
            if result.failed and not confirm('Tests failed. Continue anyway?'):
                abort('Aborting at user request.')
                break

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
    local('git push -u origin master')

def status():
    local('git status')

def add_translate(language):
    if not os.path.exists('locale'):
        os.makedirs('locale')
    local('django-admin.py makemessages -l %s' % (language))

def update_translate():
    local('django-admin.py makemessages -a')

def compile_translate():
    local('django-admin.py compilemessages')

def prepare_deploy():
    test()
    commit()
    push()

#def host_type():
#    run('uname -s')   
