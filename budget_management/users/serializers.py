from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data["username"], validated_data["password"])
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        if user is not None:
            refresh = TokenObtainPairSerializer.get_token(user)
            refresh["username"] = user.username
            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return data
        return None

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError("Username or Password is Incorrect")
        return data

    def create(self, validated_data):
        user = authenticate(username=validated_data["username"], password=validated_data["password"])
        if user is not None:
            user.is_active = True
            user.save()
        return user
