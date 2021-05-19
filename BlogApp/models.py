from django.db import models

STATUS = [
    ("A", "Active"),
    ("I", "InActive")
    ]

# Create your models here.
class BlogType(models.Model):
    type                =   models.CharField(max_length=50)
    description         =   models.TextField(max_length=100)
    status              =   models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.type