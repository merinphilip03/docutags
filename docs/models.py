from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=700)
    description = models.TextField()
    owner = models.CharField(max_length=700)
    image = models.ImageField(upload_to='documents/')
    tags = models.TextField(max_length=10000)
    upload_at = models.DateTimeField(auto_now_add=True)
    subject = models.TextField(null=True)
    department = models.TextField(max_length=2000, null=True)

    def tag_list(self):
        return self.tags.split(',')
