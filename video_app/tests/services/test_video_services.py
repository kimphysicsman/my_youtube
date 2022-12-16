from django.test import TestCase

from video_app.services.video_service import get_video_chart_most_popular

class TestVideoChartView(TestCase):
    """
        인기차트 조회 기능 테스트
    """


    def test_get_video_chart_most_popular(self):
        video_ids = get_video_chart_most_popular()

        for video_id in video_ids:
            print(video_id)