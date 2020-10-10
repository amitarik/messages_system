from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

ROOT_URL = "http://127.0.0.1:8000"
USER_URL = f"{ROOT_URL}/users"


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=False, related_name='receiver', on_delete=models.PROTECT)
    read_state = models.BooleanField(default=False)

    @property
    def get_sender_info(self) -> dict:
        data = {
            'name': self.sender.username,
            'id': self.sender.id,
            'Email': self.sender.email
        }
        return data

    @property
    def get_receiver_info(self) -> dict:
        data = {
            'name': self.receiver.username,
            'id': self.receiver.id,
            'Email': self.receiver.email
        }
        return data


class UserMessages(models.Model):
    index = models.AutoField(primary_key=True)
    message = models.ForeignKey(Message, null=False, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)  # false when the user delete the message
