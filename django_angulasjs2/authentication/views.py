from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    # we will use the username attribute of the Account model to look up accounts instead of the id attribute. Overriding lookup_field handles this for us  : https://thinkster.io/django-angularjs-tutorial/
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
        	Account.objects.create_user(**serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)