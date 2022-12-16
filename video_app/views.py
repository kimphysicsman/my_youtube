from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



class VideoChartView(APIView):
    """
        인기차트 API
    """

    def get(self, request):
        """
            인기차트 조회 API
        """

        return Response({}, status=status.HTTP_200_OK)