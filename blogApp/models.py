from django.db import models
from django.utils import timezone
# Create your models here.

# admin is admin
# password is test4321

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    created_date=  models.DateTimeField(default=timezone.now())
    # (should be populated with current dat/time when record created)
    published_date=  models.DateTimeField(default=timezone.now(),blank = True, null=True)
    # (should be populated when record created and if updated)

    def __str__(self):
        return self.title
    # makes it easier to read inside the admin