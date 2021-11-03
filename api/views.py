from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status, response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from gestion_prochette.models import Pochette
from .serializers import users, pochette
from django.middleware import csrf
from django.http import JsonResponse
from .permissions import IsAuthorOrReadOnly
from itertools import chain
from django.contrib.auth import get_user_model


class PochetteList(ListCreateAPIView):
    """ List, Create views for music album covers from gestion_prochette """
    serializer_class = pochette.PochetteSerializer

    def get_queryset(self):
        """
            This view return a list of public pochette covers
            and user no-public covers when authenticated
        """
        user = self.request.user

        if user:
            public_pochettes = Pochette.objects.filter(is_public=True)
            user_no_pub_pochettes = Pochette.objects.filter(author=user.id)

            return set(chain(public_pochettes, user_no_pub_pochettes))
        else:
            return Pochette.objects.filter(is_public=True)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = pochette.PochetteSerializer(data=data)

        if serializer.is_valid():
            try:
                v_data = serializer.validated_data
                Pochette.objects.create(
                    title=v_data['title'],
                    image=v_data['image'],
                    image_for_detail_page=data['image'],
                    author=self.request.user,
                    is_public=v_data['is_public'],
                )

                return response.Response('Commande executer avec success',
                                         status=status.HTTP_201_CREATED)
            except Exception as error:
                return response.Response(
                    error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                raise error

        #  Return 400 if serializer is invalid

        return response.Response('Something wrong ! Please repeat later.',
                                 status=status.HTTP_400_BAD_REQUEST)


class PochetteDetails(RetrieveUpdateDestroyAPIView):
    """ Get, Update, Detele Views for album covers from gestion_prochette """
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Pochette.objects.all()
    serializer_class = pochette.PochetteSerializer


#  Return CSRF token
def get_csrf_token(request):
    token = csrf.get_token(request)

    return JsonResponse({'csrf_token': token})
