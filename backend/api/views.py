from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, NoteSerializer, PlotSerializer, PlotCaseSerializer, PlotPictureSerializer, PlotMapSerializer, PlotSaleSerializer, PlotPriceSerializer, FavoriteSerializer
from .models import Note, Plot, PlotCase, PlotMap, PlotPicture, PlotPrice, PlotSale, Favorite
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class GetUserView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        print(User.objects.filter(id=self.request.user.id))
        return User.objects.filter(id=self.request.user.id)

        
class PlotCaseViewSet(viewsets.ViewSet):
    queryset = PlotCase.objects
    permission_classes = [AllowAny]
    def list(self, request):
        serializer_class = PlotCaseSerializer(self.queryset.all(), many=True)
        return Response(serializer_class.data)

class PlotViewSet(viewsets.ViewSet):
    queryset = Plot.objects
    permission_classes = [AllowAny]

    def list(self, request):
        serializer_class = PlotSerializer(self.queryset.all(), many=True)
        return Response(serializer_class.data)
    
    def listByType(self, request, plot_type=None):
        post = get_object_or_404(self.queryset.all(), plot_type=plot_type, many=True)
        serializer_class = PlotSerializer(post)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PlotSerializer(post)
        return Response(serializer_class.data)
    
class PlotPictureViewSet(viewsets.ViewSet):
    queryset = PlotPicture.objects
    permission_classes = [AllowAny]
    def list(self, request):
        serializer_class = PlotPictureSerializer(self.queryset.all(), many=True)
        return Response(serializer_class.data)
    
class PlotMapViewSet(viewsets.ViewSet):
    queryset = PlotMap.objects
    permission_classes = [AllowAny]
    def list(self, request):
        serializer_class = PlotMapSerializer(self.queryset.all(), many=True)
        return Response(serializer_class.data)
    
class PlotSaleViewSet(viewsets.ViewSet):
    queryset = PlotSale.objects
    permission_classes = [AllowAny]
    def list(self, request):
        serializer_class = PlotSaleSerializer(self.queryset.all(), many=True)
        return Response(serializer_class.data)

class PlotPriceViewSet(viewsets.ViewSet):
    queryset = PlotPrice.objects
    permission_classes = [AllowAny]
    def list(self, request):
        serializer_class = PlotPriceSerializer(self.queryset.all(), many=True)
        return Response(serializer_class.data)

class FavoriteViewSet(viewsets.ViewSet):
    queryset = Favorite.objects
    permission_classes = [AllowAny]
    def list(self, request):
        serializer_class = FavoriteSerializer(self.queryset.all(), many=True)
        return Response(serializer_class.data)