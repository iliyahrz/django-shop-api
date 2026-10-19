from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .iliya import ProductSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


# @method_decorator(login_required)
class ProductAPIView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, r, slug):
        mahsool = get_object_or_404(Product, slug=slug)
        serialize = ProductSerializer(mahsool) # Json
        return Response(serialize.data, status=200)
        

class ProductListAPIView(APIView):  # Request
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request):
        hameye_mahsoolat = Product.objects.all()  # SQL
        serialize = ProductSerializer(hameye_mahsoolat, many=True) # Json
        return Response(serialize.data, status=200)  # Response
    
