from rest_framework import serializers
from .models import RawVideo, RenderedVideo


class RawVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawVideo
        fields = "__all__"


class RenderedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenderedVideo
        fields = "__all__"


class InsertTextInputSerializer(serializers.Serializer):
    raw_video_id = serializers.IntegerField()
    text = serializers.CharField()
    position = serializers.CharField()
