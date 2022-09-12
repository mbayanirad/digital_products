from dataclasses import fields
from fileinput import filename
from pyexpat import model
from statistics import mode

from rest_framework import serializers

from .models import Category, Product,File


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'avatar', 'url')

class FileSerializer(serializers.ModelSerializer):
    fileType = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('id','title', 'fileType', 'file')
    
    def get_fileType(self, obj):
        return obj.get_fileType_display()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    #how add additional field to serializer
    meysam = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('meysam', 'title', 'description', 'avatar', 'categories', 'files', 'url')
    
    def get_meysam(self, obj):
        return 'Meysam is {}'.format(obj.id)