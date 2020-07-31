from django.db import models
from django.contrib.auth.models import User
class Notification(models.Model):
    heading = models.CharField(max_length = 20)
    user = models.ForeignKey(to=User,on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now_add = True)
    url = models.URLField(null=True)
    seen = models.BooleanField(default=False)
    def __str__(self):
        return self.heading
