from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Plot, PlotCase, PlotMap, PlotPicture, PlotPrice, PlotSale, Favorite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'

class PlotCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotCase
        fields = '__all__'

class PlotMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotMap
        fields = '__all__'

class PlotPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotPicture
        fields = '__all__'

class PlotPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotPrice
        fields = '__all__'

class PlotSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotSale
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        extra_kwargs = {"user": {"read_only": True}}

    # def create(self, validated_data):
    #     print(validated_data)
    #     user = User.objects.create_user(**validated_data)
    #     return user