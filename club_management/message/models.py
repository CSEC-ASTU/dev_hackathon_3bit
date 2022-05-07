from pyclbr import Class
from django.db import models
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your models here.
User = get_user_model()





class Send(models.Model):  # new
    text = models.TextField()

    def __str__(self):  # new
        return self.text[:10]
  


        
class Chat(models.Model):
    admin = models.ForeignKey(User)
    participants = models.ManyToManyField(User, related_name='chats')
    created = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    user = models.ForeignKey(User)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500) # what length you want