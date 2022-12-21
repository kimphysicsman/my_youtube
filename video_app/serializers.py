from django.utils import timezone 

from rest_framework import serializers

from video_app.models import ChartModel


class ChartModelSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    def get_date(self, obj):
        # utc로 저장된 datetime을 현재 timezone으로 변경
        date = obj.date.astimezone(timezone.get_current_timezone())
        return date.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ChartModel
        fields = "__all__"