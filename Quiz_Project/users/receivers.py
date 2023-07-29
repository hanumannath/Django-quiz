from django.dispatch import receiver
from .signals import *
from .models import *

@receiver(login_logging)
def my_task_done(sender, user, **kwargs):
    LoginLogs.objects.create(user=user)
    print(sender, user)