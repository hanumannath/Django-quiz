from django.db import models
from django.contrib.auth.models import User

class LoginLogs(models.Model):
    USER_TYPE_CHOICES = (
        ('A', 'Admin'),
        ('U', 'User'),
    )
    user = models.ForeignKey(User, related_name="login_logs", on_delete=models.CASCADE)
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    login_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} logged in at {self.login_at}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = 'A' if self.user.is_staff else 'U'
        super(LoginLogs, self).save(*args, **kwargs)
