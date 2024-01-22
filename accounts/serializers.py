from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth.password_validation import validate_password
from accounts.AuthBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout

# rest_framework JWT token Class Import
from rest_framework_simplejwt.tokens import RefreshToken
import json


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    # password = serializers.CharField(min_length=8)

    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "message",
            "status",
            "access",
            "refresh",
        )

    def create(self, validated_data):
        return validated_data

    def validate(self, data):
        email = data["email"]
        password = data["password"]
        user = EmailBackend.authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            # update_last_login(None, user)

            validation = {
                "access": access_token,
                "refresh": refresh_token,
                "email": user.email,
                "message": "Successfully login",
                "status": status.HTTP_200_OK,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
