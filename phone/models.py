from django.db import models

# Create your models here.
class Phone(models.Model):
    title=models.CharField(max_length=400)
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

1

