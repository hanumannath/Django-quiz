from django import dispatch
import django.dispatch

login_logging = django.dispatch.Signal("user")