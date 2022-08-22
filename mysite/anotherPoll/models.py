from email import message
from pyexpat import model
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_pic = models.ImageField()
    is_active = models.BooleanField(default=False)
    last_seen = models.DateTimeField("last seen date time")


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_msg = models.ForeignKey()
    msg_id = models.CharField(max_length=20)
    msg_body = models.CharField(max_length=300)
    create_date = models.DateTimeField("Message create date time")


class Group(models.Model):
    members = models.ManyToManyField(User)
    group_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField("Date group was created")
    is_active = models.BooleanField(default=False)


class message_recipient(models.Model):
    recipient = models.OneToOneField(User)
    message = models.OneToOneField(Message)
    is_read = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
