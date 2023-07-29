
from .models import *


def login_handler(user):
    LoginLogs.objects.create(user=user)
    print(user)