from django.db import models

# Create your models h
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    diri=models.TextField()

    def __str__(self):
        return self.name
class person(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pics')
    diri1=models.TextField()

    def __str__(self):
        return self.name1