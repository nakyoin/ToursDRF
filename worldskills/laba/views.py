from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .permissions import *
from .serializers import *
from rest_framework.generics import *




class TourApiView(ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class SingleTourChange(RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    authentication_classes = (TokenAuthentication, )

class SingleTourView(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class ProfileApiView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication, )

class SingleProfileView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication, )

class CountryApiView(ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )

class SingleCountryView(RetrieveUpdateDestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )

class ExcApiView(ListCreateAPIView):
    queryset = Excourses.objects.all()
    serializer_class = ExcSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )

class SingleExcView(RetrieveUpdateDestroyAPIView):
    queryset = Excourses.objects.all()
    serializer_class = ExcSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )