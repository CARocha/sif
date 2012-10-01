from fabric.api import run, local, hosts, cd
from fabric.contrib import django
from django.conf import settings

django.settings_module('settings')

def dump_production_database():
    run('mysqldump -u %s -p=%s %s > /home/crocha/prod-db.sql' % (
         settings.DATABASE_USER,
         settings.DATABASE_PASSWORD,
         settings.DATABASE_NAME
        ))
