from rest_framework import serializers
from base.models import Profile, Content, Order
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "id", "email", "name", "isAdmin"]

    def get_name(self, obj):
        name = obj.first_name
        if (name == ""):
            name = obj.email
        return name

    def get_isAdmin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "id", "email", "token", "isAdmin", "profile"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_profile(self, obj):
        profile = obj.profile
        sr = ProfileSerializer(profile, many=False)
        return sr.data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]


class ProfileSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "id", "profileImage"]


class ContentSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)

    class Meta:
        model = Content
        fields = "__all__"


class ContentSubSerializer(serializers.ModelSerializer):
    owner = ProfileSubSerializer(many=False)
    totalLikes = serializers.SerializerMethodField()

    class Meta:
        model = Content
        exclude = ["likes"]

    def get_totalLikes(self, obj):
        totalLikes = obj.number_of_likes()
        return totalLikes


class OrderSerializer(serializers.ModelSerializer):
    buyer = ProfileSubSerializer(many=False)

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemsSerializer(serializers.ModelSerializer):
    buyer = ProfileSubSerializer(many=False)
    orderItems = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_orderItems(self, obj):
        sr = ContentSubSerializer(obj.orderItems, many=True)
        return sr.data
