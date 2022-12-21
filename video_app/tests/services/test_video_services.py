from django.test import TestCase

from video_app.services.video_service import (
    get_video_chart_most_popular,
    save_video_chart,
    get_video_chart_list,
)

from video_app.models import ChartModel

class TestVideoChartView(TestCase):
    """
        인기차트 조회 기능 테스트
    """
    

    # def test_get_video_chart_most_popular(self):
    #     video_ids = get_video_chart_most_popular()

    #     for video_id in video_ids:
    #         print(video_id)

    # def test_save_video_chart(self):
    #     video_chart = {
    #         "rank_1": "test_1",
    #         "rank_2": "test_2",
    #         "rank_3": "test_3",
    #         "rank_4": "test_4",
    #         "rank_5": "test_5"
    #         }

    #     instance_info = save_video_chart(video_chart)
    #     if instance_info:
    #         print(instance_info)
    #     else:
    #         print("저장실패")

    # def test_get_video_chart_list(self):
    #     temp = {
    #         "rank_1": "test_1",
    #         "rank_2": "test_2",
    #         "rank_3": "test_3",
    #         "rank_4": "test_4",
    #         "rank_5": "test_5"
    #         }

    #     ChartModel.objects.create(**temp)
    #     ChartModel.objects.create(**temp)
    #     ChartModel.objects.create(**temp)

    #     chart_list = get_video_chart_list()

    #     print(chart_list)