from creators.models import Creator, Content

from rest_framework import serializers


class CreatorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Creator model.
    """

    class Meta:
        model = Creator
        fields = ["name", "username", "rating", "platform"]


class ContentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Content model.
    """

    creator = CreatorSerializer()
    is_video = serializers.BooleanField()

    class Meta:
        model = Content
        fields = ["url", "created", "modified", "creator", "is_video"]
