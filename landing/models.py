from django.db import models

# Create your models here.
class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img_url = models.URLField()
    page = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


