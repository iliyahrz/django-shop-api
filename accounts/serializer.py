from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "phone", "password"]

    def create(self, validated_data): # save()
        user = CustomUser.objects.create_user(**validated_data) # INSERT INTO CustomUser VALUES ()

        return user
    


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("نام کاربری یا رمز عبور اشتباه است.")

        if not user.is_active:
            raise serializers.ValidationError("حساب کاربری غیرفعال است.")

        refresh = RefreshToken.for_user(user)

        data["user"] = user
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data