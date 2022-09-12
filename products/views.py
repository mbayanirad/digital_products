from itertools import product
from multiprocessing import context
from django.shortcuts import render
from .models import Category, Product, File
from .serializer import CategorySerializer, ProductSerializer, FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products import serializer

# Create your views here.

#---------------------- Product View ----------------------------
class ProductListView(APIView):

    def get(self, req):
        products = Product.objects.all()
        print('-' * 10)
        print(product)
        serializer = ProductSerializer(products, many=True, context={'request':req})
        if serializer.is_valid:
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ProductDetailView(APIView):
    def get(self, req, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': req})
        return Response(serializer.data)


#---------------------- Category View ----------------------------

class CategoryListView(APIView):
    
    def get(self, req):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True, context={'request':req})
        return Response(serializer.data)



class CategoryDetailView(APIView):
    def get(self, req, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, context={'request':req})
        return Response(serializer.data)

    
#---------------------- File View ----------------------------

class FileListView(APIView):

    def get(self, req, product_pk):
        files = File.objects.filter(product_id=product_pk)
        serializer = FileSerializer(files, many=True, context={'request':req})
        return Response(serializer.data)

class FileDetailView(APIView):

    def get(self, req, product_pk, pk):
        try:
            file = File.objects.get(product_id=product_pk, pk=pk)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(file, context={'request':req})
        return Response(serializer.data)           
