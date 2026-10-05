from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .iliya import ProductSerializer


class ProductAPIView(APIView):
    def get(self, r, slug):
        mahsool = get_object_or_404(Product, slug=slug)
        serialize = ProductSerializer(mahsool) # Json
        return Response(serialize.data, status=200)
        

class ProductListAPIView(APIView):  # Request
    def get(self, request):
        hameye_mahsoolat = Product.objects.all()  # SQL
        serialize = ProductSerializer(hameye_mahsoolat, many=True) # Json
        return Response(serialize.data, status=200)  # Response
    
