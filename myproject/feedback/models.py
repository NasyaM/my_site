from django.db import models

class Feedback(models.Model):
       full_name = models.CharField(max_length=255)
       email = models.EmailField()
       text = models.TextField()
       is_verified = models.BooleanField(default=False)

       def __str__(self):
           return f"{self.full_name} - {self.email}"