import json

import pymysql
pymysql.install_as_MySQLdb()

from django.template.defaultfilters import register

@register.filter('to_json')
def to_json(value):
    obj = value.__dict__
    if '_state' in obj.keys():
        obj.pop('_state')

    return json.dumps(obj)