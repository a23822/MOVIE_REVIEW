import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe
 
register = template.Library()
 
# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size):
    default = "https://www.gravatar.com/avatar/"
    res = default + hashlib.md5(email.encode('utf-8')).hexdigest() + '?s=' + str(size)
    return res