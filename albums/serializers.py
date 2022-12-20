from rest_framework import serializers
from users.models import User

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Album
        fields= ["id", "name", "year", "user_id"]
    
    def get_user_id(self, obj:User):
        return obj.id


# class AlbumSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     year = serializers.IntegerField()
#     user_id = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         return Album.objects.create(**validated_data)
