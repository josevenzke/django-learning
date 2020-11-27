from django.db import models

# Create your models here.
class User(models.Model):
    us_fname = models.CharField(max_length=264)
    us_lname = models.CharField(max_length=264)
    us_email = models.EmailField(max_length=264)

    def __str__(self):
        return self.us_fname+" "+self.us_lname
