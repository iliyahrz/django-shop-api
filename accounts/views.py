from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer, LoginSerializer
    
class SignupAPIView(APIView):

    def post(self, request):

        serializer = SignupSerializer(data=request.data) # request.POST
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "ثبت نام با موفقیت انجام شد.","user": {"id": user.id,"username": user.username,"email": user.email}},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoginAPIView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            return Response({
                    "message": "ورود موفق بود.","access": serializer.validated_data["access"],
                    "refresh": serializer.validated_data["refresh"],
                    "user": {"id": serializer.validated_data["user"].id,"username": serializer.validated_data["user"].username,}},
                status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)