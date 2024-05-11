from django.db import models


class Movie(models.Model):  #Movie table definition
    name=models.CharField(max_length=30)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='movies',null=True,blank=True)

    def __str__(self):
        return self.name