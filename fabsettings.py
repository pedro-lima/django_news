import os
import sys

PROJECT_FULL_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
sys.path.append(PROJECT_FULL_PATH)

myproject = PROJECT_FULL_PATH.split('/')[-1] + ".settings"
myproject = __import__(myproject)
INSTALLED_APPS = ( app for app in  myproject.settings.INSTALLED_APPS if not "django" in app )
