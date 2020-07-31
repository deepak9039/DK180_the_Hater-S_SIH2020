# templatetags/custom_tags.py
from django import template
# from home.models import Notification

register = template.Library()
@register.filter
def count_notification(thing):
    if type(thing) == str:
        return 0
    return thing.filter(seen=False).count()


