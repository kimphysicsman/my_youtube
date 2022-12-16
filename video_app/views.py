from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from video_app.services.video_service import get_video_chart_most_popular


class VideoChartView(APIView):
    """
        인기차트 API
    """

    def get(self, request):
        """
            인기차트 조회 API
        """

        video_ids = get_video_chart_most_popular()

        return Response({"video_ids": video_ids}, status=status.HTTP_200_OK)