from django.db import models

class Checklist(models.Model):
    name = models.CharField(max_length=100)
    is_required = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name}"
