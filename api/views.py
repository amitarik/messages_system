from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, MessageSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Message


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('username',)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Message to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # filtering fields
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['read_state', 'title', 'sender__username', 'receiver__username',
                        'sender__id', 'receiver__id', ]



