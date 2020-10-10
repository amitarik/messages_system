from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Message
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SenderUserField(serializers.Field):

    def to_representation(self, value):
        return value.get_sender_info

    def to_internal_value(self, value):
        user_obj = User.objects.get(pk=value)
        ret = {'sender': user_obj}
        return ret


class ReceiverUserField(serializers.Field):

    def to_representation(self, value):
        return value.get_receiver_info

    def to_internal_value(self, value):
        user_obj = User.objects.get(pk=value)
        ret = {'receiver': user_obj}
        return ret


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = SenderUserField(source='*')
    receiver = ReceiverUserField(source='*')

    class Meta:
        model = Message
        fields = ['url', 'message_id', 'title', 'content', 'date_posted', 'sender', 'receiver', 'read_state',]


