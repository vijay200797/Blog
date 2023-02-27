from django.db import models

POST_TYPE = [
    (1, "Link"),
    (2, "Video"),
    (3, "Article")
]

POST_STATUS = [
    (1, "Active"),
    (0, "InActive")
]

# Create your models here.
class Post(models.Model):
    post_title                              =   models.CharField(max_length=100)
    post_content                            =   models.CharField(max_length=200)
    post_type                               =   models.IntegerField(choices=POST_TYPE)
    post_datetime                           =   models.DateTimeField(auto_now_add=True)
    post_status                             =   models.IntegerField(choices=POST_STATUS)
    post_additionalContext                  =   models.CharField(max_length=200)

    def __str__(self):
        return self.post_title
