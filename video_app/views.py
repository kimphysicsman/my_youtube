from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from video_app.services.video_service import (
    get_video_chart_most_popular,
    save_video_chart,
    get_video_chart_list,
    )


class VideoChartView(APIView):
    """
        인기차트 API
    """

    def get(self, request):
        """
            인기차트 조회 API
        """

        try:
            video_ids = get_video_chart_most_popular()
        except:
            return Response({"error": "조회에 실패했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(video_ids, status=status.HTTP_200_OK)

    def post(self, request):
        """
            인기차트 저장 API
        """

        if save_video_chart(request.data):
            return Response({"message": "저장 성공"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "저장에 실패했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class VideoChartListView(APIView):
    def get(self, request):
        try:
            chart_list = get_video_chart_list()
        except:
            return Response({"error": "조회에 실패했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(chart_list, status=status.HTTP_200_OK)