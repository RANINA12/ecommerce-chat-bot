from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    model_name = models.CharField(max_length=100)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model_name

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_type = models.CharField(max_length=50)
    user_input = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} at {self.timestamp}"
